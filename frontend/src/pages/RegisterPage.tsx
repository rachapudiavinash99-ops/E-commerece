import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { User, Mail, Lock, Code, ArrowRight } from 'lucide-react';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';

export const RegisterPage: React.FC = () => {
  const { register, isLoading } = useAuthStore();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<'student' | 'instructor'>('student');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage(null);
    try {
      await register({
        full_name: fullName,
        email,
        password,
        role
      });
      navigate(role === 'instructor' ? '/instructor/dashboard' : '/student/dashboard');
    } catch (err: any) {
      setErrorMessage(err.response?.data?.detail || 'Registration failed. Email might already exist.');
    }
  };

  return (
    <div className="max-w-md mx-auto px-4 py-16 space-y-8">
      <div className="text-center space-y-2">
        <div className="inline-flex p-3 bg-brand-500/10 rounded-2xl text-brand-400 border border-brand-500/20 mb-2">
          <Code className="w-6 h-6" />
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Create an Account</h1>
        <p className="text-xs text-slate-400">Join thousands of developers mastering modern full-stack engineering</p>
      </div>

      <form onSubmit={handleSubmit} className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-5 shadow-2xl">
        {errorMessage && (
          <div className="p-3.5 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs font-medium">
            {errorMessage}
          </div>
        )}

        <Input
          label="Full Name"
          type="text"
          placeholder="e.g. Sarah Connor"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          leftIcon={<User className="w-4 h-4" />}
          required
        />

        <Input
          label="Email Address"
          type="email"
          placeholder="e.g. sarah@example.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          leftIcon={<Mail className="w-4 h-4" />}
          required
        />

        <Input
          label="Password (min. 6 chars)"
          type="password"
          placeholder="••••••••••••"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          leftIcon={<Lock className="w-4 h-4" />}
          required
          minLength={6}
        />

        {/* Role selection */}
        <div className="space-y-1.5">
          <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
            I want to:
          </label>
          <div className="grid grid-cols-2 gap-3">
            <button
              type="button"
              onClick={() => setRole('student')}
              className={`p-3 rounded-xl border text-xs font-bold transition-all ${
                role === 'student'
                  ? 'bg-brand-500/20 border-brand-500 text-brand-300'
                  : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              Learn Courses
            </button>
            <button
              type="button"
              onClick={() => setRole('instructor')}
              className={`p-3 rounded-xl border text-xs font-bold transition-all ${
                role === 'instructor'
                  ? 'bg-brand-500/20 border-brand-500 text-brand-300'
                  : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              Teach & Build
            </button>
          </div>
        </div>

        <Button
          type="submit"
          variant="primary"
          className="w-full font-bold shadow-lg shadow-brand-500/20"
          isLoading={isLoading}
          rightIcon={<ArrowRight className="w-4 h-4" />}
        >
          Create Account
        </Button>

        <p className="text-center text-xs text-slate-400 pt-2">
          Already have an account?{' '}
          <Link to="/login" className="text-brand-400 hover:text-brand-300 font-semibold">
            Sign In
          </Link>
        </p>
      </form>
    </div>
  );
};
