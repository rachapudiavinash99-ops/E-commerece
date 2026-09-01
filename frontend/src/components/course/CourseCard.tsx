import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Clock, BarChart, Users, ShoppingCart, Check } from 'lucide-react';
import { Course } from '../../types';
import { RatingStars } from '../common/RatingStars';
import { Badge } from '../common/Badge';
import { Button } from '../common/Button';
import { useCartStore } from '../../store/cartStore';

interface CourseCardProps {
  course: Course;
  isEnrolled?: boolean;
}

export const CourseCard: React.FC<CourseCardProps> = ({ course, isEnrolled = false }) => {
  const { addToCart, cart } = useCartStore();
  const navigate = useNavigate();

  const isItemInCart = cart?.items.some((item) => item.course_id === course.id);

  const handleAddToCart = async (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
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

  return (
    <Link
      to={`/courses/${course.slug}`}
      className="group flex flex-col bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-2xl overflow-hidden transition-all duration-300 hover:shadow-2xl hover:shadow-brand-500/10 hover:-translate-y-1"
    >
      {/* Thumbnail */}
      <div className="relative aspect-video w-full overflow-hidden bg-slate-950">
        <img
          src={course.thumbnail_url || 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600'}
          alt={course.title}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-transparent to-transparent opacity-80" />

        {/* Top Badges */}
        <div className="absolute top-3 left-3 flex flex-wrap gap-1.5">
          {course.is_bestseller && <Badge variant="gold">Bestseller</Badge>}
          {course.is_featured && !course.is_bestseller && <Badge variant="brand">Featured</Badge>}
        </div>

        {/* Level Tag */}
        <div className="absolute bottom-3 left-3">
          <span className="px-2 py-0.5 text-[10px] font-semibold bg-slate-900/90 text-slate-300 rounded border border-slate-700 capitalize">
            {course.level.replace('_', ' ')}
          </span>
        </div>
      </div>

      {/* Content */}
      <div className="flex flex-col flex-1 p-5 space-y-3">
        {/* Topic & Instructor */}
        <div className="flex items-center justify-between text-xs text-slate-400">
          <span className="font-semibold text-brand-400">{course.topic?.name || 'Software Engineering'}</span>
          <span>{course.instructor?.full_name || 'CodePulse Faculty'}</span>
        </div>

        {/* Title */}
        <h3 className="font-bold text-sm text-slate-100 group-hover:text-brand-300 transition-colors line-clamp-2 leading-snug">
          {course.title}
        </h3>

        {/* Subtitle snippet */}
        <p className="text-xs text-slate-400 line-clamp-2 leading-relaxed">
          {course.short_description || course.subtitle || course.description}
        </p>

        {/* Rating & Stats */}
        <div className="pt-1">
          <RatingStars rating={course.average_rating} reviewCount={course.review_count} size={14} />
        </div>

        {/* Meta Info */}
        <div className="flex items-center gap-4 text-xs text-slate-400 pt-1 border-t border-slate-800/80">
          <div className="flex items-center gap-1">
            <Clock className="w-3.5 h-3.5 text-slate-500" />
            <span>{course.duration_hours}h</span>
          </div>
          <div className="flex items-center gap-1">
            <Users className="w-3.5 h-3.5 text-slate-500" />
            <span>{course.student_count} students</span>
          </div>
        </div>

        {/* Price & Action */}
        <div className="mt-auto pt-3 flex items-center justify-between border-t border-slate-800">
          <div className="flex items-baseline gap-2">
            <span className="text-lg font-black text-white">
              ${course.discount_price !== undefined && course.discount_price !== null ? course.discount_price.toFixed(2) : course.price.toFixed(2)}
            </span>
            {course.discount_price !== undefined && course.discount_price !== null && course.discount_price < course.price && (
              <span className="text-xs text-slate-500 line-through">
                ${course.price.toFixed(2)}
              </span>
            )}
          </div>

          <Button
            size="sm"
            variant={isEnrolled ? 'success' : isItemInCart ? 'secondary' : 'primary'}
            onClick={handleAddToCart}
            leftIcon={isEnrolled ? <Check className="w-3.5 h-3.5" /> : <ShoppingCart className="w-3.5 h-3.5" />}
          >
            {isEnrolled ? 'Enrolled' : isItemInCart ? 'In Cart' : 'Add to Cart'}
          </Button>
        </div>
      </div>
    </Link>
  );
};
