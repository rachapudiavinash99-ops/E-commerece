import React, { useEffect, useState } from 'react';
import { User, Course, Category, Topic } from '../types';
import { apiClient } from '../api/client';
import { 
  Shield, Users, BookOpen, DollarSign, CheckCircle2, 
  XCircle, Plus, Tag, Layers, RefreshCw 
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import { Modal } from '../components/common/Modal';
import { Input } from '../components/common/Input';

export const AdminDashboardPage: React.FC = () => {
  const [analytics, setAnalytics] = useState<any>(null);
  const [users, setUsers] = useState<User[]>([]);
  const [courses, setCourses] = useState<Course[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [activeTab, setActiveTab] = useState<'overview' | 'courses' | 'users' | 'taxonomy' | 'coupons'>('overview');
  const [isLoading, setIsLoading] = useState(true);

  // New Category / Topic Modal
  const [isCatModalOpen, setIsCatModalOpen] = useState(false);
  const [isTopicModalOpen, setIsTopicModalOpen] = useState(false);
  const [isCouponModalOpen, setIsCouponModalOpen] = useState(false);

  const [catName, setCatName] = useState('');
  const [topicName, setTopicName] = useState('');
  const [topicCatId, setTopicCatId] = useState<number>(1);
  const [couponCode, setCouponCode] = useState('');
  const [couponDiscount, setCouponDiscount] = useState('20');

  const fetchAdminData = async () => {
    try {
      const [aRes, uRes, cRes, catRes] = await Promise.all([
        apiClient.get('/admin/analytics'),
        apiClient.get<User[]>('/admin/users'),
        apiClient.get<any>('/courses?page_size=50'),
        apiClient.get<Category[]>('/categories')
      ]);
      setAnalytics(aRes.data);
      setUsers(uRes.data);
      setCourses(cRes.data.items);
      setCategories(catRes.data);
    } catch (err) {
      console.error('Failed to load admin data', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchAdminData();
  }, []);

  const handleApproveCourse = async (courseId: number, status: 'published' | 'rejected') => {
    try {
      await apiClient.put(`/admin/courses/${courseId}/status`, { status });
      fetchAdminData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleUpdateRole = async (userId: number, newRole: string) => {
    try {
      await apiClient.put(`/admin/users/${userId}/role`, { role: newRole });
      fetchAdminData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreateCategory = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiClient.post('/admin/categories', {
        name: catName,
        slug: catName.toLowerCase().replace(/[^a-z0-9]+/g, '-')
      });
      setIsCatModalOpen(false);
      setCatName('');
      fetchAdminData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreateTopic = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiClient.post('/admin/topics', {
        category_id: topicCatId,
        name: topicName,
        slug: topicName.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
        is_popular: true
      });
      setIsTopicModalOpen(false);
      setTopicName('');
      fetchAdminData();
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreateCoupon = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiClient.post('/admin/coupons', {
        code: couponCode.toUpperCase(),
        discount_type: 'percentage',
        discount_value: parseFloat(couponDiscount),
        minimum_amount: 10.0,
        usage_limit: 500,
        active: true
      });
      setIsCouponModalOpen(false);
      setCouponCode('');
      fetchAdminData();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-2">
            <Shield className="w-5 h-5 text-amber-400" />
            <h1 className="text-3xl font-extrabold text-white tracking-tight">Admin Operations Command Center</h1>
          </div>
          <p className="text-xs text-slate-400 mt-1">Platform management, topic taxonomy, and course moderation</p>
        </div>

        <div className="flex gap-2">
          <Button size="sm" variant="outline" onClick={() => setIsCatModalOpen(true)} leftIcon={<Plus className="w-3.5 h-3.5" />}>
            New Category
          </Button>
          <Button size="sm" variant="outline" onClick={() => setIsTopicModalOpen(true)} leftIcon={<Plus className="w-3.5 h-3.5" />}>
            New Topic
          </Button>
          <Button size="sm" variant="primary" onClick={() => setIsCouponModalOpen(true)} leftIcon={<Tag className="w-3.5 h-3.5" />}>
            Create Coupon
          </Button>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="flex gap-2 border-b border-slate-800 pb-2 text-xs font-semibold">
        {(['overview', 'courses', 'users', 'taxonomy'] as const).map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-2 rounded-lg capitalize transition-colors ${
              activeTab === tab ? 'bg-brand-500 text-white' : 'text-slate-400 hover:text-white hover:bg-slate-900'
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Overview Analytics Tab */}
      {activeTab === 'overview' && analytics && (
        <div className="space-y-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
              <span className="text-slate-400 text-xs font-medium">Total Platform Users</span>
              <div className="text-2xl font-black text-white">{analytics.total_users}</div>
            </div>
            <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
              <span className="text-slate-400 text-xs font-medium">Published Courses</span>
              <div className="text-2xl font-black text-brand-400">{analytics.published_courses}</div>
            </div>
            <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
              <span className="text-slate-400 text-xs font-medium">Total Gross Revenue</span>
              <div className="text-2xl font-black text-emerald-400">${analytics.total_revenue.toFixed(2)}</div>
            </div>
            <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-1">
              <span className="text-slate-400 text-xs font-medium">Active Enrollments</span>
              <div className="text-2xl font-black text-amber-400">{analytics.total_enrollments}</div>
            </div>
          </div>
        </div>
      )}

      {/* Courses Tab */}
      {activeTab === 'courses' && (
        <div className="rounded-2xl border border-slate-800 bg-slate-900 overflow-hidden shadow-xl">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950 text-slate-400 uppercase font-semibold border-b border-slate-800 text-[10px]">
              <tr>
                <th className="p-4">Title</th>
                <th className="p-4">Instructor</th>
                <th className="p-4">Price</th>
                <th className="p-4">Status</th>
                <th className="p-4">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-850">
              {courses.map((course) => (
                <tr key={course.id} className="hover:bg-slate-850/50">
                  <td className="p-4 font-bold text-white">{course.title}</td>
                  <td className="p-4">{course.instructor?.full_name}</td>
                  <td className="p-4">${course.price.toFixed(2)}</td>
                  <td className="p-4"><Badge variant={course.status === 'published' ? 'success' : 'warning'}>{course.status}</Badge></td>
                  <td className="p-4 flex gap-2">
                    {course.status !== 'published' && (
                      <Button size="sm" variant="success" onClick={() => handleApproveCourse(course.id, 'published')}>
                        Approve
                      </Button>
                    )}
                    {course.status === 'published' && (
                      <Button size="sm" variant="danger" onClick={() => handleApproveCourse(course.id, 'rejected')}>
                        Unpublish
                      </Button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Users Tab */}
      {activeTab === 'users' && (
        <div className="rounded-2xl border border-slate-800 bg-slate-900 overflow-hidden shadow-xl">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950 text-slate-400 uppercase font-semibold border-b border-slate-800 text-[10px]">
              <tr>
                <th className="p-4">User</th>
                <th className="p-4">Email</th>
                <th className="p-4">Role</th>
                <th className="p-4">Status</th>
                <th className="p-4">Promote</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-850">
              {users.map((u) => (
                <tr key={u.id} className="hover:bg-slate-850/50">
                  <td className="p-4 font-bold text-white">{u.full_name}</td>
                  <td className="p-4">{u.email}</td>
                  <td className="p-4 font-semibold text-brand-400 capitalize">{u.role}</td>
                  <td className="p-4"><Badge variant={u.is_active ? 'success' : 'danger'}>{u.is_active ? 'Active' : 'Banned'}</Badge></td>
                  <td className="p-4 flex gap-1.5">
                    {u.role !== 'admin' && (
                      <Button size="sm" variant="outline" onClick={() => handleUpdateRole(u.id, 'admin')}>
                        Make Admin
                      </Button>
                    )}
                    {u.role !== 'instructor' && (
                      <Button size="sm" variant="secondary" onClick={() => handleUpdateRole(u.id, 'instructor')}>
                        Make Instructor
                      </Button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Taxonomy Tab */}
      {activeTab === 'taxonomy' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {categories.map((cat) => (
            <div key={cat.id} className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-3">
              <h4 className="font-bold text-sm text-white flex items-center gap-2">
                <Layers className="w-4 h-4 text-brand-400" />
                <span>{cat.name}</span>
              </h4>
              <div className="flex flex-wrap gap-2 pt-2">
                {cat.topics?.map((top) => (
                  <span key={top.id} className="px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-800 text-xs text-slate-300 font-medium">
                    {top.name}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* New Category Modal */}
      <Modal isOpen={isCatModalOpen} onClose={() => setIsCatModalOpen(false)} title="Create New Category">
        <form onSubmit={handleCreateCategory} className="space-y-4">
          <Input label="Category Name" placeholder="e.g. Artificial Intelligence" value={catName} onChange={(e) => setCatName(e.target.value)} required />
          <Button type="submit" variant="primary" className="w-full">Create Category</Button>
        </form>
      </Modal>

      {/* New Topic Modal */}
      <Modal isOpen={isTopicModalOpen} onClose={() => setIsTopicModalOpen(false)} title="Create Database-Driven Topic">
        <form onSubmit={handleCreateTopic} className="space-y-4">
          <div className="space-y-1.5">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Parent Category</label>
            <select value={topicCatId} onChange={(e) => setTopicCatId(Number(e.target.value))} className="w-full bg-slate-900 border border-slate-800 rounded-lg p-2.5 text-xs text-white">
              {categories.map((c) => (<option key={c.id} value={c.id}>{c.name}</option>))}
            </select>
          </div>
          <Input label="Topic Name" placeholder="e.g. PyTorch & Neural Networks" value={topicName} onChange={(e) => setTopicName(e.target.value)} required />
          <Button type="submit" variant="primary" className="w-full">Create Topic</Button>
        </form>
      </Modal>

      {/* New Coupon Modal */}
      <Modal isOpen={isCouponModalOpen} onClose={() => setIsCouponModalOpen(false)} title="Create Promotional Coupon">
        <form onSubmit={handleCreateCoupon} className="space-y-4">
          <Input label="Coupon Code" placeholder="e.g. SUMMER50" value={couponCode} onChange={(e) => setCouponCode(e.target.value.toUpperCase())} required />
          <Input label="Discount Percentage (%)" type="number" value={couponDiscount} onChange={(e) => setCouponDiscount(e.target.value)} required />
          <Button type="submit" variant="primary" className="w-full">Create Coupon</Button>
        </form>
      </Modal>
    </div>
  );
};
