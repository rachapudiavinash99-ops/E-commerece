import React from 'react';
import { HelpCircle, ChevronDown } from 'lucide-react';

export const FaqPage: React.FC = () => {
  const faqs = [
    {
      q: 'How does the interactive Python sandbox work?',
      a: 'Our execution engine runs an isolated Python 3.12 runner with AST syntax safety analysis. Your code executes inside a sub-millisecond container sandbox and is verified against both public and hidden test cases.'
    },
    {
      q: 'Are certificates cryptographically verified?',
      a: 'Yes! Every issued certificate includes a unique SHA-256 HMAC cryptographic digest. Anyone can verify the authenticity of your certificate at /certificates/verify/:code.'
    },
    {
      q: 'Can I get a refund if I am not satisfied?',
      a: 'We offer a full 30-Day Money-Back Guarantee on all course purchases with zero questions asked.'
    },
    {
      q: 'Do I get lifetime access to purchased courses?',
      a: 'Yes, once purchased or enrolled, you have permanent lifetime access to all course modules, videos, coding tasks, and future curriculum updates.'
    }
  ];

  return (
    <div className="max-w-4xl mx-auto px-4 py-16 space-y-10">
      <div className="text-center space-y-3">
        <div className="inline-flex p-3 bg-brand-500/10 rounded-2xl text-brand-400 border border-brand-500/20">
          <HelpCircle className="w-8 h-8" />
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Frequently Asked Questions</h1>
        <p className="text-xs text-slate-400">Everything you need to know about learning and certifying on CodePulse</p>
      </div>

      <div className="space-y-4">
        {faqs.map((f, idx) => (
          <div key={idx} className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-2 shadow-lg">
            <h3 className="text-base font-bold text-white">{f.q}</h3>
            <p className="text-xs text-slate-300 leading-relaxed">{f.a}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
