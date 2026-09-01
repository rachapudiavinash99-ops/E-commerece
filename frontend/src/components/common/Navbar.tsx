import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, Search, Code, BookOpen, User as UserIcon, LogOut, LayoutDashboard, Shield, PlusCircle, Bell, Menu, X } from 'lucide-react';
import { useAuthStore } from '../../store/authStore';
import { useCartStore } from '../../store/cartStore';
import { Button } from './Button';

export const Navbar: React.FC = () => {
  const { user, isAuthenticated, logout } = useAuthStore();
  const { cart } = useCartStore();
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/courses?query=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  const totalCartItems = cart?.item_count || 0;

  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        {/* Brand Logo */}
        <Link to="/" className="flex items-center gap-2.5 flex-shrink-0 group">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 to-cyan-400 p-0.5 shadow-lg shadow-brand-500/20 group-hover:scale-105 transition-transform">
            <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
              <Code className="w-5 h-5 text-brand-400" />
            </div>
          </div>
          <div className="flex flex-col">
            <span className="font-black text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
              CodePulse<span className="text-brand-400">.</span>
            </span>
            <span className="text-[10px] tracking-widest uppercase font-semibold text-brand-400 -mt-1">Academy</span>
          </div>
        </Link>

        {/* Global Search Bar */}
        <form onSubmit={handleSearch} className="hidden md:flex flex-1 max-w-md relative">
          <input
            type="text"
            placeholder="Search 1,000+ coding courses, topics, or stacks..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-slate-900/90 border border-slate-800 rounded-full py-2 pl-10 pr-4 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500 transition-all shadow-inner"
          />
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-2.5 pointer-events-none" />
        </form>

        {/* Navigation Links & User Actions */}
        <div className="hidden md:flex items-center gap-4">
          <Link to="/courses" className="text-xs font-semibold text-slate-300 hover:text-brand-400 transition-colors flex items-center gap-1.5">
            <BookOpen className="w-4 h-4" />
            Explore Courses
          </Link>

          {/* Cart Button */}
          <Link to="/cart" className="relative p-2 text-slate-300 hover:text-white rounded-xl hover:bg-slate-900 border border-transparent hover:border-slate-800 transition-all">
            <ShoppingCart className="w-5 h-5" />
            {totalCartItems > 0 && (
              <span className="absolute -top-1 -right-1 bg-brand-500 text-white font-bold text-[10px] w-5 h-5 rounded-full flex items-center justify-center ring-2 ring-slate-950 animate-in zoom-in">
                {totalCartItems}
              </span>
            )}
          </Link>

          {/* User Auth Section */}
          {isAuthenticated && user ? (
            <div className="flex items-center gap-3">
              {/* Dashboard Action by Role */}
              {user.role === 'admin' ? (
                <Link to="/admin/dashboard">
                  <Button variant="secondary" size="sm" leftIcon={<Shield className="w-3.5 h-3.5 text-amber-400" />}>
                    Admin Panel
                  </Button>
                </Link>
              ) : user.role === 'instructor' ? (
                <Link to="/instructor/dashboard">
                  <Button variant="secondary" size="sm" leftIcon={<PlusCircle className="w-3.5 h-3.5 text-brand-400" />}>
                    Course Studio
                  </Button>
                </Link>
              ) : (
                <Link to="/student/dashboard">
                  <Button variant="secondary" size="sm" leftIcon={<LayoutDashboard className="w-3.5 h-3.5 text-brand-400" />}>
                    My Learning
                  </Button>
                </Link>
              )}

              {/* User Avatar & Logout */}
              <div className="flex items-center gap-2 pl-2 border-l border-slate-800">
                <Link to="/profile" className="flex items-center gap-2 group">
                  <img
                    src={user.avatar_url || `https://api.dicebear.com/7.x/initials/svg?seed=${user.full_name}`}
                    alt={user.full_name}
                    className="w-8 h-8 rounded-full ring-1 ring-brand-500/30 group-hover:ring-brand-400 transition-all object-cover"
                  />
                </Link>
                <button
                  onClick={logout}
                  title="Log out"
                  className="p-1.5 text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-lg transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            </div>
          ) : (
            <div className="flex items-center gap-2.5">
              <Link to="/login">
                <Button variant="ghost" size="sm">Sign In</Button>
              </Link>
              <Link to="/register">
                <Button variant="primary" size="sm">Get Started</Button>
              </Link>
            </div>
          )}
        </div>

        {/* Mobile menu trigger */}
        <div className="flex md:hidden items-center gap-2">
          <Link to="/cart" className="relative p-2 text-slate-300">
            <ShoppingCart className="w-5 h-5" />
            {totalCartItems > 0 && (
              <span className="absolute -top-1 -right-1 bg-brand-500 text-white font-bold text-[10px] w-4 h-4 rounded-full flex items-center justify-center">
                {totalCartItems}
              </span>
            )}
          </Link>
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="p-2 text-slate-400 hover:text-white rounded-lg"
          >
            {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </div>

      {/* Mobile dropdown */}
      {isMobileMenuOpen && (
        <div className="md:hidden border-b border-slate-800 bg-slate-950 p-4 space-y-3 animate-in slide-in-from-top duration-150">
          <form onSubmit={handleSearch} className="relative">
            <input
              type="text"
              placeholder="Search courses..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full bg-slate-900 border border-slate-800 rounded-lg py-2 pl-9 pr-4 text-xs text-slate-100"
            />
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          </form>
          <div className="pt-2 border-t border-slate-800 flex flex-col gap-2">
            <Link to="/courses" className="text-sm text-slate-300 py-1.5" onClick={() => setIsMobileMenuOpen(false)}>
              Explore Courses
            </Link>
            {isAuthenticated ? (
              <>
                <Link to="/student/dashboard" className="text-sm text-brand-400 py-1.5" onClick={() => setIsMobileMenuOpen(false)}>
                  My Learning Dashboard
                </Link>
                <button onClick={() => { logout(); setIsMobileMenuOpen(false); }} className="text-left text-sm text-rose-400 py-1.5">
                  Sign Out
                </button>
              </>
            ) : (
              <div className="flex gap-2 pt-2">
                <Link to="/login" className="flex-1" onClick={() => setIsMobileMenuOpen(false)}>
                  <Button variant="outline" size="sm" className="w-full">Sign In</Button>
                </Link>
                <Link to="/register" className="flex-1" onClick={() => setIsMobileMenuOpen(false)}>
                  <Button variant="primary" size="sm" className="w-full">Register</Button>
                </Link>
              </div>
            )}
          </div>
        </div>
      )}
    </header>
  );
};
