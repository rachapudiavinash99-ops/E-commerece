import React from 'react';
import { Check, Zap, Award, Shield, Sparkles } from 'lucide-react';
import { Button } from '../components/common/Button';
import { useNavigate } from 'react-router-dom';

export const PricingPage: React.FC = () => {
  const navigate = useNavigate();

  const tiers = [
    {
      name: 'Individual Course',
      price: 'Pay Per Course',
      desc: 'Lifetime access to specific masterclasses with verified certificate',
      features: [
        'Full HD video content & lifetime access',
        'Interactive Python 3.12 Code IDE Sandbox',
        'Automated task testing against hidden test cases',
        'Quizzes with instant answer explanations',
        'Cryptographic Certificate of Completion',
        'Direct instructor Q&A forum access'
      ],
      cta: 'Explore Courses',
      action: () => navigate('/courses'),
      featured: false
    },
    {
      name: 'All-Access Pro',
      price: '$29 / month',
      desc: 'Unlimited access to all 50+ masterclasses and upcoming releases',
      features: [
        'Everything in Individual Course Tier',
        'Unlimited access to all engineering tracks',
        'New masterclass releases every month',
        'Interactive System Design Architecture Blueprints',
        'Priority code review by Senior Staff Engineers',
        'Verified LinkedIn Digital Badge & Resume Credential',
        'Discord VIP Developer Lounge access'
      ],
      cta: 'Start 7-Day Free Trial',
      action: () => navigate('/register'),
      featured: true
    },
    {
      name: 'Enterprise Team',
      price: 'Custom',
      desc: 'Empower engineering organizations with team analytics and custom tracks',
      features: [
        'Unlimited team seats and SSO SAML authentication',
        'Dedicated company-specific coding tracks',
        'Custom private sandbox test case runners',
        'Engineering manager skill progress dashboard',
        'Dedicated Customer Success & Technical Account Lead',
        'SLA 99.99% uptime guarantee with invoice billing'
      ],
      cta: 'Contact Sales',
      action: () => navigate('/courses'),
      featured: false
    }
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
      <div className="text-center space-y-4 max-w-3xl mx-auto">
        <div className="inline-flex p-3 bg-brand-500/10 rounded-2xl text-brand-400 border border-brand-500/20">
          <Zap className="w-6 h-6" />
        </div>
        <h1 className="text-4xl font-extrabold text-white tracking-tight">Simple, Transparent Pricing</h1>
        <p className="text-sm text-slate-400">
          Choose the learning path that fits your engineering goals. Every plan includes full hands-on code sandboxes and verified certificates.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
        {tiers.map((t, idx) => (
          <div
            key={idx}
            className={`flex flex-col p-8 rounded-3xl border transition-all duration-300 ${
              t.featured
                ? 'bg-slate-900 border-brand-500/50 shadow-2xl shadow-brand-500/10 scale-105 relative'
                : 'bg-slate-900/60 border-slate-800'
            }`}
          >
            {t.featured && (
              <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 px-3 py-1 rounded-full bg-brand-500 text-white font-bold text-[11px] uppercase tracking-wider shadow-lg">
                Most Popular
              </div>
            )}

            <div className="space-y-2 pb-6 border-b border-slate-800">
              <h3 className="text-xl font-bold text-white">{t.name}</h3>
              <div className="text-2xl font-black text-brand-400">{t.price}</div>
              <p className="text-xs text-slate-400 leading-relaxed">{t.desc}</p>
            </div>

            <div className="space-y-3 py-6 flex-1 text-xs text-slate-300">
              {t.features.map((f, fIdx) => (
                <div key={fIdx} className="flex items-start gap-2.5">
                  <Check className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                  <span>{f}</span>
                </div>
              ))}
            </div>

            <Button
              variant={t.featured ? 'primary' : 'outline'}
              className="w-full font-bold mt-auto"
              onClick={t.action}
            >
              {t.cta}
            </Button>
          </div>
        ))}
      </div>
    </div>
  );
};
