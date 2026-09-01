import React, { useState } from 'react';
import { useAuthStore } from '../store/authStore';
import { apiClient } from '../api/client';
import { User, Mail, Shield, CheckCircle, Lock } from 'lucide-react';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';

export const ProfilePage: React.FC = () => {
  const { user, loadUser } = useAuthStore();

  const [headline, setHeadline] = useState(user?.headline || '');
  const [bio, setBio] = useState(user?.bio || '');
  const [oldPass, setOldPass] = useState('');
  const [newPass, setNewPass] = useState('');
  const [statusMsg, setStatusMsg] = useState<string | null>(null);

  const handleUpdateProfile = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiClient.put('/users/profile', { headline, bio });
      await loadUser();
      setStatusMsg('Profile updated successfully!');
    } catch (e) {
      console.error(e);
    }
  };

  const handleChangePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiClient.post('/users/change-password', {
        old_password: oldPass,
        new_password: newPass
      });
      setOldPass('');
      setNewPass('');
      setStatusMsg('Password changed successfully!');
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className="max-w-3xl mx-auto px-4 py-12 space-y-8">
      <div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Account Profile</h1>
        <p className="text-xs text-slate-400 mt-1">Manage your personal details and security</p>
      </div>

      {statusMsg && (
        <div className="p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold">
          {statusMsg}
        </div>
      )}

      <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6">
        <div className="flex items-center gap-4 pb-6 border-b border-slate-800">
          <img
            src={user?.avatar_url || `https://api.dicebear.com/7.x/initials/svg?seed=${user?.full_name}`}
            alt={user?.full_name}
            className="w-16 h-16 rounded-full ring-2 ring-brand-500/40 object-cover"
          />
          <div>
            <h3 className="text-lg font-bold text-white">{user?.full_name}</h3>
            <p className="text-xs text-slate-400">{user?.email}</p>
            <span className="inline-block mt-1 px-2 py-0.5 rounded text-[10px] font-bold bg-brand-500/20 text-brand-400 uppercase">
              Role: {user?.role}
            </span>
          </div>
        </div>

        {/* Profile Details Form */}
        <form onSubmit={handleUpdateProfile} className="space-y-4">
          <Input
            label="Professional Headline"
            placeholder="e.g. Senior Backend Engineer"
            value={headline}
            onChange={(e) => setHeadline(e.target.value)}
          />

          <div className="space-y-1.5">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Bio</label>
            <textarea
              rows={3}
              value={bio}
              onChange={(e) => setBio(e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-3 text-xs text-white"
              placeholder="Tell other students and instructors about yourself..."
            />
          </div>

          <Button type="submit" variant="primary" size="sm">
            Save Profile Changes
          </Button>
        </form>
      </div>

      {/* Password Form */}
      <form onSubmit={handleChangePassword} className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-4">
        <h3 className="text-sm font-bold text-white flex items-center gap-2">
          <Lock className="w-4 h-4 text-brand-400" />
          <span>Security & Password</span>
        </h3>

        <Input
          label="Current Password"
          type="password"
          value={oldPass}
          onChange={(e) => setOldPass(e.target.value)}
          required
        />

        <Input
          label="New Password"
          type="password"
          value={newPass}
          onChange={(e) => setNewPass(e.target.value)}
          required
          minLength={6}
        />

        <Button type="submit" variant="secondary" size="sm">
          Update Password
        </Button>
      </form>
    </div>
  );
};
