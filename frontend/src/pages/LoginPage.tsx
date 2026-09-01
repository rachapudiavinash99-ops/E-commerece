import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { Lock, Mail, Code, ArrowRight, ShieldCheck, Zap } from 'lucide-react';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';

export const LoginPage: React.FC = () => {
  const { login, isLoading } = useAuthStore();
  const navigate = useNavigate();
  const location = useLocation();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const from = (location.state as any)?.from?.pathname || '/';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage(null);
    try {
      await login(email, password);
      navigate(from, { replace: true });
    } catch (err: any) {
      setErrorMessage(err.response?.data?.detail || 'Invalid email or password.');
    }
  };

  const handleQuickLogin = (quickEmail: string, quickPass: string) => {
    setEmail(quickEmail);
    setPassword(quickPass);
  };

  return (
    <div className="max-w-md mx-auto px-4 py-16 space-y-8">
      <div className="text-center space-y-2">
        <div className="inline-flex p-3 bg-brand-500/10 rounded-2xl text-brand-400 border border-brand-500/20 mb-2">
          <Code className="w-6 h-6" />
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Sign In to CodePulse</h1>
        <p className="text-xs text-slate-400">Enter your credentials to access your courses and sandbox IDE</p>
      </div>

      {/* Demo Credentials Quick Pill Box */}
      <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 space-y-2.5">
        <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
          <Zap className="w-3.5 h-3.5 text-brand-400" />
          <span>Instant One-Click Test Accounts:</span>
        </span>
        <div className="grid grid-cols-3 gap-2 text-[11px]">
          <button
            type="button"
            onClick={() => handleQuickLogin('student@codepulse.io', 'StudentPass123!')}
            className="p-2 rounded-lg bg-slate-950 hover:bg-brand-500/20 text-slate-300 hover:text-brand-300 border border-slate-800 transition-colors font-semibold"
          >
            Student
          </button>
          <button
            type="button"
            onClick={() => handleQuickLogin('guido@codepulse.io', 'InstructorPass123!')}
            className="p-2 rounded-lg bg-slate-950 hover:bg-purple-500/20 text-slate-300 hover:text-purple-300 border border-slate-800 transition-colors font-semibold"
          >
            Instructor
          </button>
          <button
            type="button"
            onClick={() => handleQuickLogin('admin@codepulse.io', 'AdminPass123!')}
            className="p-2 rounded-lg bg-slate-950 hover:bg-amber-500/20 text-slate-300 hover:text-amber-300 border border-slate-800 transition-colors font-semibold"
          >
            Admin
          </button>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-5 shadow-2xl">
        {errorMessage && (
          <div className="p-3.5 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs font-medium">
            {errorMessage}
          </div>
        )}

        <Input
          label="Email Address"
          type="email"
          placeholder="e.g. student@codepulse.io"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          leftIcon={<Mail className="w-4 h-4" />}
          required
        />

        <Input
          label="Password"
          type="password"
          placeholder="••••••••••••"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          leftIcon={<Lock className="w-4 h-4" />}
          required
        />

        <Button
          type="submit"
          variant="primary"
          className="w-full font-bold shadow-lg shadow-brand-500/20"
          isLoading={isLoading}
          rightIcon={<ArrowRight className="w-4 h-4" />}
        >
          Sign In
        </Button>

        <p className="text-center text-xs text-slate-400 pt-2">
          Don't have an account?{' '}
          <Link to="/register" className="text-brand-400 hover:text-brand-300 font-semibold">
            Create an account
          </Link>
        </p>
      </form>
    </div>
  );
};
