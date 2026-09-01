import React, { useEffect, useState } from 'react';
import { Course, Topic } from '../types';
import { apiClient } from '../api/client';
import { 
  Plus, BookOpen, Users, DollarSign, Star, 
  Layers, CheckCircle, Clock, Edit3, ShieldAlert 
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import { Modal } from '../components/common/Modal';
import { Input } from '../components/common/Input';

export const InstructorDashboardPage: React.FC = () => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [analytics, setAnalytics] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  // New Course Modal state
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newTitle, setNewTitle] = useState('');
  const [newTopicId, setNewTopicId] = useState<number>(1);
  const [newPrice, setNewPrice] = useState('49.99');
  const [newDesc, setNewDesc] = useState('');
  const [isCreating, setIsCreating] = useState(false);

  const fetchInstructorData = async () => {
    try {
      const [cRes, aRes, tRes] = await Promise.all([
        apiClient.get<Course[]>('/instructor/courses'),
        apiClient.get('/instructor/analytics'),
        apiClient.get<Topic[]>('/topics/popular?limit=20')
      ]);
      setCourses(cRes.data);
      setAnalytics(aRes.data);
      setTopics(tRes.data);
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchInstructorData();
  }, []);

  const handleCreateCourse = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsCreating(true);
    try {
      await apiClient.post('/instructor/courses', {
        title: newTitle,
        slug: newTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
        topic_id: Number(newTopicId),
        price: parseFloat(newPrice),
        description: newDesc || 'Comprehensive course description.',
        level: 'all_levels'
      });
      setIsModalOpen(false);
      setNewTitle('');
      setNewDesc('');
      fetchInstructorData();
    } catch (err) {
      console.error(err);
    } finally {
      setIsCreating(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-10">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">Instructor Course Studio</h1>
          <p className="text-xs text-slate-400 mt-1">Manage curriculum, track revenue, and publish courses</p>
        </div>

        <Button
          variant="primary"
          onClick={() => setIsModalOpen(true)}
          leftIcon={<Plus className="w-4 h-4" />}
        >
          Create New Course
        </Button>
      </div>

      {/* Stats Cards */}
      {analytics && (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
            <span className="text-slate-400 text-xs font-medium">Total Courses</span>
            <div className="text-2xl font-black text-white">{analytics.total_courses}</div>
          </div>
          <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
            <span className="text-slate-400 text-xs font-medium">Total Students</span>
            <div className="text-2xl font-black text-brand-400">{analytics.total_students}</div>
          </div>
          <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
            <span className="text-slate-400 text-xs font-medium">Instructor Revenue</span>
            <div className="text-2xl font-black text-emerald-400">${analytics.total_revenue.toFixed(2)}</div>
          </div>
          <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
            <span className="text-slate-400 text-xs font-medium">Average Rating</span>
            <div className="text-2xl font-black text-amber-400">{analytics.average_rating.toFixed(1)} ★</div>
          </div>
        </div>
      )}

      {/* Courses Management Table */}
      <div className="space-y-4">
        <h3 className="text-lg font-bold text-white tracking-tight">My Authored Courses</h3>

        <div className="rounded-2xl border border-slate-800 bg-slate-900 overflow-hidden shadow-xl">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs text-slate-300">
              <thead className="bg-slate-950 text-slate-400 uppercase font-semibold border-b border-slate-800 text-[10px] tracking-wider">
                <tr>
                  <th className="p-4">Course Title</th>
                  <th className="p-4">Topic</th>
                  <th className="p-4">Price</th>
                  <th className="p-4">Status</th>
                  <th className="p-4">Students</th>
                  <th className="p-4">Rating</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-850">
                {courses.map((course) => (
                  <tr key={course.id} className="hover:bg-slate-850/50 transition-colors">
                    <td className="p-4 font-bold text-white">{course.title}</td>
                    <td className="p-4 text-brand-400">{course.topic?.name || 'Programming'}</td>
                    <td className="p-4 font-semibold">${course.price.toFixed(2)}</td>
                    <td className="p-4">
                      <Badge variant={course.status === 'published' ? 'success' : 'neutral'}>
                        {course.status}
                      </Badge>
                    </td>
                    <td className="p-4 font-semibold text-slate-200">{course.student_count}</td>
                    <td className="p-4 font-semibold text-amber-400">{course.average_rating.toFixed(1)} ★</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Create Course Modal */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title="Create New Course"
        maxWidth="lg"
      >
        <form onSubmit={handleCreateCourse} className="space-y-4">
          <Input
            label="Course Title"
            placeholder="e.g. Master Modern Rust & WebAssembly"
            value={newTitle}
            onChange={(e) => setNewTitle(e.target.value)}
            required
          />

          <div className="space-y-1.5">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
              Topic
            </label>
            <select
              value={newTopicId}
              onChange={(e) => setNewTopicId(Number(e.target.value))}
              className="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-xs text-white"
            >
              {topics.map((t) => (
                <option key={t.id} value={t.id}>{t.name}</option>
              ))}
            </select>
          </div>

          <Input
            label="Price ($ USD)"
            type="number"
            step="0.01"
            value={newPrice}
            onChange={(e) => setNewPrice(e.target.value)}
            required
          />

          <div className="space-y-1.5">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
              Description
            </label>
            <textarea
              rows={4}
              value={newDesc}
              onChange={(e) => setNewDesc(e.target.value)}
              className="w-full bg-slate-900 border border-slate-800 rounded-lg p-3 text-xs text-white"
              placeholder="What will students learn in this course?"
              required
            />
          </div>

          <Button type="submit" variant="primary" className="w-full font-bold" isLoading={isCreating}>
            Create Course Draft
          </Button>
        </form>
      </Modal>
    </div>
  );
};
