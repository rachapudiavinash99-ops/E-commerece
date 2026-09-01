import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Terminal, Zap, Award, BookOpen, ArrowRight, CheckCircle2, Star, Users, Code, Shield } from 'lucide-react';
import { Course, Topic } from '../types';
import { apiClient } from '../api/client';
import { CourseGrid } from '../components/course/CourseGrid';
import { Button } from '../components/common/Button';

export const HomePage: React.FC = () => {
  const [featuredCourses, setFeaturedCourses] = useState<Course[]>([]);
  const [bestsellerCourses, setBestsellerCourses] = useState<Course[]>([]);
  const [popularTopics, setPopularTopics] = useState<Topic[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchHomeData = async () => {
      try {
        const [featRes, bestRes, topRes] = await Promise.all([
          apiClient.get('/courses/featured?limit=4'),
          apiClient.get('/courses/bestsellers?limit=4'),
          apiClient.get('/topics/popular?limit=8')
        ]);
        setFeaturedCourses(featRes.data);
        setBestsellerCourses(bestRes.data);
        setPopularTopics(topRes.data);
      } catch (err) {
        console.error('Failed to load homepage data', err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchHomeData();
  }, []);

  return (
    <div className="space-y-24 pb-20">
      {/* Hero Section */}
      <section className="relative pt-12 pb-20 overflow-hidden">
        {/* Ambient Glows */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[300px] bg-brand-500/15 blur-[120px] pointer-events-none rounded-full" />
        <div className="absolute top-1/3 left-1/4 w-[400px] h-[250px] bg-purple-500/10 blur-[100px] pointer-events-none rounded-full" />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative text-center space-y-8">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-brand-500/30 bg-brand-500/10 text-brand-300 text-xs font-semibold tracking-wide uppercase shadow-inner">
            <Zap className="w-3.5 h-3.5 text-brand-400" />
            <span>Interactive Code Sandbox & Verified Crypto Certificates</span>
          </div>

          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white max-w-4xl mx-auto leading-[1.1]">
            Master Full-Stack <br />
            <span className="bg-gradient-to-r from-brand-400 via-cyan-300 to-indigo-400 bg-clip-text text-transparent">
              Engineering with Real Code.
            </span>
          </h1>

          <p className="text-base sm:text-lg text-slate-400 max-w-2xl mx-auto leading-relaxed">
            The modern educational marketplace for developers. Build real-world applications in Python, React, FastAPI, and Distributed Systems with instant automated evaluation.
          </p>

          <div className="flex flex-wrap items-center justify-center gap-4 pt-2">
            <Button
              size="lg"
              variant="primary"
              onClick={() => navigate('/courses')}
              rightIcon={<ArrowRight className="w-5 h-5" />}
            >
              Explore Course Catalog
            </Button>
            <Button
              size="lg"
              variant="outline"
              onClick={() => navigate('/certificates/verify/CERT-CP-2026-DEMO99')}
              leftIcon={<Award className="w-5 h-5 text-amber-400" />}
            >
              Verify Certificate
            </Button>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto pt-12 border-t border-slate-800/80">
            <div className="space-y-1">
              <div className="text-2xl sm:text-3xl font-black text-white">100%</div>
              <div className="text-xs text-slate-400 font-medium">Hands-On Code Sandbox</div>
            </div>
            <div className="space-y-1">
              <div className="text-2xl sm:text-3xl font-black text-white">50K+</div>
              <div className="text-xs text-slate-400 font-medium">Lines of Production Code</div>
            </div>
            <div className="space-y-1">
              <div className="text-2xl sm:text-3xl font-black text-white">4.9/5</div>
              <div className="text-xs text-slate-400 font-medium">Student Review Rating</div>
            </div>
            <div className="space-y-1">
              <div className="text-2xl sm:text-3xl font-black text-white">Instant</div>
              <div className="text-xs text-slate-400 font-medium">Automated Evaluation</div>
            </div>
          </div>
        </div>
      </section>

      {/* Popular Topics Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-white tracking-tight">Popular Engineering Topics</h2>
            <p className="text-xs text-slate-400">Database-driven categories and modern development stacks</p>
          </div>
          <Link to="/courses" className="text-xs font-semibold text-brand-400 hover:text-brand-300 flex items-center gap-1">
            View all <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-4 gap-4">
          {popularTopics.map((topic) => (
            <Link
              key={topic.id}
              to={`/courses?query=${encodeURIComponent(topic.name)}`}
              className="p-4 rounded-xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-brand-500/40 flex items-center gap-3.5 group transition-all"
            >
              <div className="w-10 h-10 rounded-lg bg-brand-500/10 text-brand-400 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Code className="w-5 h-5" />
              </div>
              <div>
                <h4 className="text-sm font-bold text-slate-100 group-hover:text-brand-300 transition-colors">{topic.name}</h4>
                <p className="text-[11px] text-slate-500">{topic.description || 'Master core concepts'}</p>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Featured Courses */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-white tracking-tight">Featured Masterclasses</h2>
            <p className="text-xs text-slate-400">Hand-picked by industry engineering leads</p>
          </div>
          <Link to="/courses" className="text-xs font-semibold text-brand-400 hover:text-brand-300 flex items-center gap-1">
            Browse catalog <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <CourseGrid courses={featuredCourses} isLoading={isLoading} />
      </section>

      {/* Interactive Sandbox Feature Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="relative rounded-3xl bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 border border-slate-800 p-8 sm:p-12 overflow-hidden shadow-2xl">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
            <div className="space-y-6">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-semibold">
                <Terminal className="w-3.5 h-3.5" />
                <span>Zero Installation Required</span>
              </div>
              <h3 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                Solve Real Tasks Inside the Embedded Code IDE
              </h3>
              <p className="text-sm text-slate-300 leading-relaxed">
                Every lesson features test-driven coding challenges. Write code in the browser, run automated unit tests against hidden test cases, and receive immediate architectural feedback.
              </p>
              <div className="space-y-2.5 text-xs text-slate-300">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-brand-400" />
                  <span>Real-time Python 3.12 sandbox execution</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-brand-400" />
                  <span>Automated test assertion matcher with execution metrics</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-brand-400" />
                  <span>Interactive quizzes with instant explanations</span>
                </div>
              </div>
            </div>

            {/* Code IDE Card Visual */}
            <div className="rounded-xl bg-slate-950 border border-slate-800 shadow-2xl p-4 font-mono text-xs text-slate-300 space-y-3">
              <div className="flex items-center justify-between pb-3 border-b border-slate-800 text-[11px] text-slate-500">
                <span className="flex items-center gap-2">
                  <span className="w-2.5 h-2.5 rounded-full bg-red-500" />
                  <span className="w-2.5 h-2.5 rounded-full bg-yellow-500" />
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
                  <span className="text-slate-400 ml-2">solution.py</span>
                </span>
                <span className="text-emerald-400 font-bold">ALL TESTS PASSED (3/3)</span>
              </div>
              <pre className="text-slate-300 overflow-x-auto leading-relaxed">
{`def calculate_discount(price: float, percent: float) -> float:
    discount = price * (percent / 100.0)
    return round(price - discount, 2)`}
              </pre>
              <div className="pt-3 border-t border-slate-800 text-[11px] text-slate-400 flex items-center justify-between">
                <span>Execution Time: <strong className="text-white">12.4ms</strong></span>
                <span className="text-emerald-400 font-semibold">Score: 10 / 10 Points</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Bestselling Courses */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-white tracking-tight">Bestselling Courses</h2>
            <p className="text-xs text-slate-400">Highest enrolled engineering roadmaps</p>
          </div>
          <Link to="/courses?sort=bestseller" className="text-xs font-semibold text-brand-400 hover:text-brand-300 flex items-center gap-1">
            View all bestsellers <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <CourseGrid courses={bestsellerCourses} isLoading={isLoading} />
      </section>
    </div>
  );
};
