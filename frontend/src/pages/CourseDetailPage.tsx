import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Course, Module } from '../types';
import { apiClient } from '../api/client';
import { useCartStore } from '../store/cartStore';
import { useAuthStore } from '../store/authStore';
import { RatingStars } from '../components/common/RatingStars';
import { Badge } from '../components/common/Badge';
import { Button } from '../components/common/Button';
import { Modal } from '../components/common/Modal';
import { 
  PlayCircle, Clock, Users, Globe, ShieldCheck, CheckCircle2, 
  BookOpen, Terminal, HelpCircle, ShoppingCart, Award, Sparkles 
} from 'lucide-react';

export const CourseDetailPage: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const navigate = useNavigate();
  const { addToCart, cart } = useCartStore();
  const { isAuthenticated } = useAuthStore();

  const [course, setCourse] = useState<Course | null>(null);
  const [curriculum, setCurriculum] = useState<Module[]>([]);
  const [isEnrolled, setIsEnrolled] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [isPreviewModalOpen, setIsPreviewModalOpen] = useState(false);

  useEffect(() => {
    const fetchCourseData = async () => {
      if (!slug) return;
      try {
        const res = await apiClient.get<Course>(`/courses/${slug}`);
        setCourse(res.data);

        // Fetch curriculum
        const curRes = await apiClient.get<Module[]>(`/curriculum/courses/${res.data.id}`);
        setCurriculum(curRes.data);

        // Check enrollment if logged in
        if (isAuthenticated) {
          try {
            const enrRes = await apiClient.get(`/learning/courses/${res.data.id}`);
            if (enrRes.status === 200) setIsEnrolled(true);
          } catch (e) {
            setIsEnrolled(false);
          }
        }
      } catch (err) {
        console.error('Failed to load course', err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchCourseData();
  }, [slug, isAuthenticated]);

  if (isLoading || !course) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-20 animate-pulse space-y-6">
        <div className="h-10 bg-slate-900 rounded w-1/3" />
        <div className="h-40 bg-slate-900 rounded" />
      </div>
    );
  }

  const isItemInCart = cart?.items.some((item) => item.course_id === course.id);

  const handleEnrollOrCart = async () => {
    if (isEnrolled) {
      navigate(`/learning/course/${course.id}`);
      return;
    }
    if (isItemInCart) {
      navigate('/cart');
      return;
    }
    await addToCart(course.id);
  };

  const handleBuyNow = async () => {
    if (!isItemInCart) {
      await addToCart(course.id);
    }
    navigate('/checkout');
  };

  const whatYouWillLearnList = course.what_you_will_learn
    ? course.what_you_will_learn.split(',').map((s) => s.trim())
    : ['Write idiomatic clean code', 'Master modern architecture', 'Complete interactive test-driven tasks'];

  return (
    <div className="pb-24">
      {/* Course Hero Banner */}
      <section className="bg-slate-900/80 border-b border-slate-800 py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-3 gap-10 items-start">
          <div className="lg:col-span-2 space-y-4">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-bold text-brand-400 uppercase tracking-wide">{course.topic?.name}</span>
              {course.is_bestseller && <Badge variant="gold">Bestseller</Badge>}
              <span className="text-xs text-slate-500">•</span>
              <span className="text-xs text-slate-400 capitalize">{course.level.replace('_', ' ')}</span>
            </div>

            <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight leading-tight">
              {course.title}
            </h1>

            <p className="text-sm sm:text-base text-slate-300 leading-relaxed">
              {course.subtitle || course.short_description}
            </p>

            <div className="flex flex-wrap items-center gap-4 text-xs text-slate-400 pt-2">
              <RatingStars rating={course.average_rating} reviewCount={course.review_count} size={16} />
              <div className="flex items-center gap-1.5">
                <Users className="w-4 h-4 text-slate-500" />
                <span>{course.student_count} students enrolled</span>
              </div>
              <div className="flex items-center gap-1.5">
                <Globe className="w-4 h-4 text-slate-500" />
                <span>{course.language}</span>
              </div>
            </div>

            <div className="pt-2 text-xs text-slate-400">
              Created by <strong className="text-slate-200">{course.instructor?.full_name || 'CodePulse Faculty'}</strong>
            </div>
          </div>

          {/* Sticky Enrollment Card */}
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-2xl space-y-6 lg:sticky lg:top-24">
            {/* Promo Video Thumbnail */}
            <div
              onClick={() => setIsPreviewModalOpen(true)}
              className="relative aspect-video w-full rounded-2xl overflow-hidden cursor-pointer group bg-slate-950 border border-slate-800"
            >
              <img
                src={course.thumbnail_url || 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600'}
                alt={course.title}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform"
              />
              <div className="absolute inset-0 bg-slate-950/40 flex items-center justify-center group-hover:bg-slate-950/20 transition-colors">
                <div className="w-12 h-12 rounded-full bg-brand-500 text-white flex items-center justify-center shadow-lg shadow-brand-500/30 group-hover:scale-110 transition-transform">
                  <PlayCircle className="w-6 h-6 ml-0.5" />
                </div>
              </div>
            </div>

            {/* Pricing Details */}
            <div className="space-y-1">
              <div className="flex items-baseline gap-3">
                <span className="text-3xl font-black text-white">
                  ${course.discount_price !== undefined && course.discount_price !== null ? course.discount_price.toFixed(2) : course.price.toFixed(2)}
                </span>
                {course.discount_price !== undefined && course.discount_price !== null && course.discount_price < course.price && (
                  <span className="text-sm text-slate-500 line-through">
                    ${course.price.toFixed(2)}
                  </span>
                )}
              </div>
              <p className="text-[11px] text-emerald-400 font-semibold flex items-center gap-1">
                <Sparkles className="w-3 h-3" /> Full lifetime access with verified certificate
              </p>
            </div>

            {/* Actions */}
            <div className="space-y-2.5">
              <Button
                variant={isEnrolled ? 'success' : isItemInCart ? 'secondary' : 'primary'}
                className="w-full py-3 text-sm font-bold"
                onClick={handleEnrollOrCart}
                leftIcon={isEnrolled ? <BookOpen className="w-4 h-4" /> : <ShoppingCart className="w-4 h-4" />}
              >
                {isEnrolled ? 'Go to Course Player' : isItemInCart ? 'View in Cart' : 'Add to Cart'}
              </Button>

              {!isEnrolled && (
                <Button
                  variant="outline"
                  className="w-full py-3 text-sm font-bold"
                  onClick={handleBuyNow}
                >
                  Buy Now
                </Button>
              )}
            </div>

            {/* Includes List */}
            <div className="space-y-2 pt-4 border-t border-slate-800 text-xs text-slate-300">
              <h4 className="font-bold text-slate-200">This masterclass includes:</h4>
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-brand-400" />
                <span>{course.duration_hours} hours of on-demand HD video</span>
              </div>
              <div className="flex items-center gap-2">
                <Terminal className="w-4 h-4 text-brand-400" />
                <span>Embedded interactive coding exercises</span>
              </div>
              <div className="flex items-center gap-2">
                <HelpCircle className="w-4 h-4 text-brand-400" />
                <span>Quizzes with detailed answer breakdowns</span>
              </div>
              <div className="flex items-center gap-2">
                <Award className="w-4 h-4 text-brand-400" />
                <span>Verified cryptographic Certificate of Completion</span>
              </div>
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-emerald-400" />
                <span>30-Day Money-Back Guarantee</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Course Body: What you will learn, Curriculum, Requirements */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 grid grid-cols-1 lg:grid-cols-3 gap-10">
        <div className="lg:col-span-2 space-y-12">
          {/* What You Will Learn */}
          <div className="p-6 rounded-2xl bg-slate-900/40 border border-slate-800 space-y-4">
            <h3 className="text-lg font-bold text-white tracking-tight">What You Will Learn</h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-300">
              {whatYouWillLearnList.map((item, idx) => (
                <div key={idx} className="flex items-start gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Curriculum Section */}
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <h3 className="text-xl font-bold text-white tracking-tight">Course Curriculum</h3>
              <span className="text-xs text-slate-400">{curriculum.length} modules</span>
            </div>

            <div className="space-y-3">
              {curriculum.map((mod, modIdx) => (
                <div key={mod.id} className="border border-slate-800 rounded-xl bg-slate-900/60 overflow-hidden">
                  <div className="p-4 bg-slate-900/90 font-bold text-sm text-slate-200 flex items-center justify-between">
                    <span>{mod.title}</span>
                    <span className="text-xs text-slate-400 font-normal">{mod.lessons.length} lessons</span>
                  </div>
                  <div className="divide-y divide-slate-850">
                    {mod.lessons.map((lesson) => (
                      <div key={lesson.id} className="p-3.5 px-5 flex items-center justify-between text-xs text-slate-300 hover:bg-slate-850/50 transition-colors">
                        <div className="flex items-center gap-3">
                          {lesson.lesson_type === 'video' ? (
                            <PlayCircle className="w-4 h-4 text-brand-400" />
                          ) : lesson.lesson_type === 'coding_task' ? (
                            <Terminal className="w-4 h-4 text-emerald-400" />
                          ) : (
                            <HelpCircle className="w-4 h-4 text-amber-400" />
                          )}
                          <span>{lesson.title}</span>
                        </div>
                        <div className="flex items-center gap-3">
                          {lesson.is_preview && <Badge variant="brand" size="sm">Preview</Badge>}
                          <span className="text-slate-500">{lesson.duration_minutes} min</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Description */}
          <div className="space-y-4">
            <h3 className="text-xl font-bold text-white tracking-tight">Description</h3>
            <div className="prose prose-invert max-w-none text-xs text-slate-300 leading-relaxed whitespace-pre-line">
              {course.description}
            </div>
          </div>
        </div>
      </section>

      {/* Preview Modal */}
      <Modal
        isOpen={isPreviewModalOpen}
        onClose={() => setIsPreviewModalOpen(false)}
        title="Course Preview"
        maxWidth="2xl"
      >
        <div className="aspect-video w-full rounded-xl overflow-hidden bg-black">
          <iframe
            src={course.promo_video_url || 'https://www.youtube.com/embed/kqtD5dpn9C8'}
            title="Course Promo"
            className="w-full h-full"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      </Modal>
    </div>
  );
};
