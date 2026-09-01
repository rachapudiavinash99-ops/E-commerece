import React from 'react';
import { Link } from 'react-router-dom';
import { Code, Github, Twitter, Linkedin, ShieldCheck, Award, Zap, Heart } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-slate-900 bg-slate-950/90 text-slate-400 text-xs mt-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14 grid grid-cols-1 md:grid-cols-5 gap-10">
        {/* Brand Col */}
        <div className="md:col-span-2 space-y-4">
          <Link to="/" className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-cyan-400 p-0.5">
              <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
                <Code className="w-4 h-4 text-brand-400" />
              </div>
            </div>
            <span className="font-bold text-base tracking-tight text-white">
              CodePulse<span className="text-brand-400">.</span>Academy
            </span>
          </Link>
          <p className="text-slate-400 leading-relaxed max-w-sm text-xs">
            Commercial-grade engineering platform featuring real-time Python/JavaScript code evaluation sandboxes, verified cryptographic certifications, and database-driven curriculum mastery.
          </p>
          <div className="flex items-center gap-3 pt-2">
            <a href="https://github.com/rachapudiavinash99-ops/E-commerece.git" target="_blank" rel="noreferrer" className="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors border border-slate-800">
              <Github className="w-4 h-4" />
            </a>
            <a href="#" className="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors border border-slate-800">
              <Twitter className="w-4 h-4" />
            </a>
            <a href="#" className="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors border border-slate-800">
              <Linkedin className="w-4 h-4" />
            </a>
          </div>
        </div>

        {/* Col 1 */}
        <div className="space-y-3">
          <h4 className="font-bold text-slate-100 uppercase tracking-wider text-[11px]">Popular Stacks</h4>
          <ul className="space-y-2">
            <li><Link to="/courses?query=Python" className="hover:text-brand-400 transition-colors">Python 3.12 Masterclass</Link></li>
            <li><Link to="/courses?query=FastAPI" className="hover:text-brand-400 transition-colors">FastAPI Microservices</Link></li>
            <li><Link to="/courses?query=React" className="hover:text-brand-400 transition-colors">React 18 & TypeScript</Link></li>
            <li><Link to="/courses?query=Algorithms" className="hover:text-brand-400 transition-colors">Data Structures & DSA</Link></li>
            <li><Link to="/courses?query=Docker" className="hover:text-brand-400 transition-colors">Docker & DevOps</Link></li>
          </ul>
        </div>

        {/* Col 2 */}
        <div className="space-y-3">
          <h4 className="font-bold text-slate-100 uppercase tracking-wider text-[11px]">Platform</h4>
          <ul className="space-y-2">
            <li><Link to="/courses" className="hover:text-brand-400 transition-colors">Course Marketplace</Link></li>
            <li><Link to="/student/dashboard" className="hover:text-brand-400 transition-colors">Student Learning Hub</Link></li>
            <li><Link to="/certificates/verify/CERT-CP-2026-DEMO99" className="hover:text-brand-400 transition-colors">Certificate Registry</Link></li>
            <li><Link to="/instructor/dashboard" className="hover:text-brand-400 transition-colors">Teach on CodePulse</Link></li>
            <li><Link to="/admin/dashboard" className="hover:text-brand-400 transition-colors">Admin Command Suite</Link></li>
          </ul>
        </div>

        {/* Col 3 */}
        <div className="space-y-3">
          <h4 className="font-bold text-slate-100 uppercase tracking-wider text-[11px]">Trust & Security</h4>
          <div className="space-y-2 text-slate-400">
            <div className="flex items-center gap-1.5 text-emerald-400 font-medium">
              <ShieldCheck className="w-4 h-4" />
              <span>256-Bit Encrypted Payments</span>
            </div>
            <div className="flex items-center gap-1.5 text-amber-400 font-medium">
              <Award className="w-4 h-4" />
              <span>Verified Crypto Certificates</span>
            </div>
            <div className="flex items-center gap-1.5 text-brand-400 font-medium">
              <Zap className="w-4 h-4" />
              <span>Live Code Execution</span>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 border-t border-slate-900/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-500">
        <p>&copy; {new Date().getFullYear()} CodePulse Academy, Inc. All rights reserved.</p>
        <p className="flex items-center gap-1">
          Engineered with <Heart className="w-3 h-3 text-rose-500 fill-rose-500" /> for elite full-stack developers.
        </p>
      </div>
    </footer>
  );
};
