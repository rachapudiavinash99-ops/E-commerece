import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Enrollment, Certificate, User } from '../types';
import { apiClient } from '../api/client';
import { useAuthStore } from '../store/authStore';
import { 
  BookOpen, Award, Clock, CheckCircle2, PlayCircle, 
  ArrowRight, Sparkles, Trophy, Download 
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import { EmptyState } from '../components/common/EmptyState';

export const StudentDashboardPage: React.FC = () => {
  const { user } = useAuthStore();
  const navigate = useNavigate();

  const [enrollments, setEnrollments] = useState<Enrollment[]>([]);
  const [certificates, setCertificates] = useState<Certificate[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const [enrRes, certRes] = await Promise.all([
          apiClient.get<Enrollment[]>('/learning/enrollments'),
          apiClient.get<Certificate[]>('/certificates')
        ]);
        setEnrollments(enrRes.data);
        setCertificates(certRes.data);
      } catch (err) {
        console.error('Failed to load student dashboard', err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchDashboard();
  }, []);

  const inProgressCount = enrollments.filter((e) => !e.is_completed).length;
  const completedCount = enrollments.filter((e) => e.is_completed).length;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
      {/* Welcome Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-8 rounded-3xl bg-gradient-to-r from-brand-900/40 via-slate-900 to-slate-900 border border-brand-500/20 shadow-2xl">
        <div className="space-y-2">
          <span className="text-xs font-bold uppercase tracking-wider text-brand-400">Student Learning Hub</span>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Welcome back, {user?.full_name}!
          </h1>
          <p className="text-xs text-slate-400">Continue building your full-stack engineering proficiency.</p>
        </div>
        <Button
          variant="primary"
          onClick={() => navigate('/courses')}
          rightIcon={<BookOpen className="w-4 h-4" />}
        >
          Explore Catalog
        </Button>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
          <span className="text-slate-400 text-xs font-medium">Enrolled Courses</span>
          <div className="text-2xl font-black text-white">{enrollments.length}</div>
        </div>
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
          <span className="text-slate-400 text-xs font-medium">In Progress</span>
          <div className="text-2xl font-black text-brand-400">{inProgressCount}</div>
        </div>
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
          <span className="text-slate-400 text-xs font-medium">Completed Courses</span>
          <div className="text-2xl font-black text-emerald-400">{completedCount}</div>
        </div>
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
          <span className="text-slate-400 text-xs font-medium">Certificates Earned</span>
          <div className="text-2xl font-black text-amber-400">{certificates.length}</div>
        </div>
      </div>

      {/* Enrolled Courses Grid */}
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-white tracking-tight">My Courses</h2>
          <span className="text-xs text-slate-400">{enrollments.length} enrolled</span>
        </div>

        {enrollments.length === 0 ? (
          <EmptyState
            icon={<BookOpen className="w-8 h-8" />}
            title="No Enrolled Courses"
            description="You haven't enrolled in any programming courses yet."
            actionText="Discover Courses"
            onAction={() => navigate('/courses')}
          />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {enrollments.map((enr) => (
              <div
                key={enr.id}
                className="flex flex-col p-5 rounded-2xl bg-slate-900/60 border border-slate-800 hover:border-slate-700 transition-all space-y-4 shadow-xl"
              >
                <div className="aspect-video w-full rounded-xl overflow-hidden bg-slate-950">
                  <img
                    src={enr.course.thumbnail_url || 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600'}
                    alt={enr.course.title}
                    className="w-full h-full object-cover"
                  />
                </div>

                <div className="space-y-1 flex-1">
                  <span className="text-[10px] font-bold text-brand-400 uppercase tracking-wider">
                    {enr.course.topic?.name || 'Programming'}
                  </span>
                  <h3 className="font-bold text-sm text-white line-clamp-2">{enr.course.title}</h3>
                </div>

                {/* Progress bar */}
                <div className="space-y-1.5 pt-2">
                  <div className="flex justify-between text-xs font-semibold">
                    <span className="text-slate-400">Completion</span>
                    <span className={enr.is_completed ? 'text-emerald-400' : 'text-brand-400'}>
                      {enr.completion_percentage.toFixed(0)}%
                    </span>
                  </div>
                  <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
                    <div
                      className={`h-2 rounded-full transition-all duration-500 ${
                        enr.is_completed ? 'bg-emerald-500' : 'bg-brand-500'
                      }`}
                      style={{ width: `${enr.completion_percentage}%` }}
                    />
                  </div>
                </div>

                <Button
                  variant={enr.is_completed ? 'success' : 'primary'}
                  size="sm"
                  className="w-full font-bold"
                  onClick={() => navigate(`/learning/course/${enr.course_id}`)}
                  leftIcon={<PlayCircle className="w-4 h-4" />}
                >
                  {enr.is_completed ? 'Review Course' : 'Continue Learning'}
                </Button>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Earned Certificates Gallery */}
      {certificates.length > 0 && (
        <div className="space-y-6 pt-6 border-t border-slate-800">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-bold text-white tracking-tight flex items-center gap-2">
              <Trophy className="w-5 h-5 text-amber-400" />
              <span>Earned Certificates</span>
            </h2>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {certificates.map((cert) => (
              <div
                key={cert.id}
                className="p-6 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-950 border border-amber-500/20 space-y-4 shadow-xl"
              >
                <div className="flex items-center justify-between">
                  <Badge variant="gold">Verified Certificate</Badge>
                  <span className="text-[11px] font-mono text-amber-400 font-bold">{cert.certificate_number}</span>
                </div>

                <div className="space-y-1">
                  <h4 className="font-bold text-sm text-white">{cert.course?.title || 'Programming Masterclass'}</h4>
                  <p className="text-xs text-slate-400">Issued on {new Date(cert.issued_at).toLocaleDateString()}</p>
                </div>

                <div className="flex gap-2 pt-2">
                  <Button
                    size="sm"
                    variant="outline"
                    className="flex-1"
                    onClick={() => navigate(`/certificates/verify/${cert.verification_code}`)}
                  >
                    Verify Online
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
