import React from 'react';
import { MessageSquare, Users, ThumbsUp, MessageCircle, Sparkles, Pin } from 'lucide-react';
import { Button } from '../components/common/Button';

export const CommunityForumPage: React.FC = () => {
  const threads = [
    {
      id: 1,
      title: 'Python 3.12 GIL removal & subinterpreters performance benchmarks in production',
      author: 'Guido Rossum',
      replies: 42,
      likes: 128,
      category: 'Python Architecture',
      pinned: true,
      timeAgo: '2 hours ago'
    },
    {
      id: 2,
      title: 'How to handle idempotency keys in high-throughput FastAPI payment webhooks?',
      author: 'Sarah Connor',
      replies: 19,
      likes: 54,
      category: 'FastAPI & Payments',
      pinned: false,
      timeAgo: '5 hours ago'
    },
    {
      id: 3,
      title: 'Best practices for React 18 Server Components vs Client Components with Zustand',
      author: 'Brendan Eich',
      replies: 31,
      likes: 89,
      category: 'React & Frontend',
      pinned: false,
      timeAgo: '1 day ago'
    }
  ];

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-2">
            <MessageSquare className="w-6 h-6 text-brand-400" />
            <h1 className="text-3xl font-extrabold text-white tracking-tight">Developer Community Q&A</h1>
          </div>
          <p className="text-xs text-slate-400 mt-1">Discuss coding challenges, share system designs, and learn with peers</p>
        </div>

        <Button variant="primary" size="sm">
          Ask New Question
        </Button>
      </div>

      <div className="space-y-4">
        {threads.map((t) => (
          <div
            key={t.id}
            className="p-6 rounded-2xl bg-slate-900 border border-slate-800 hover:border-slate-700 transition-all space-y-3 shadow-lg"
          >
            <div className="flex items-center gap-2">
              {t.pinned && (
                <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-brand-500/20 text-brand-400 text-[10px] font-bold uppercase">
                  <Pin className="w-3 h-3" /> Pinned
                </span>
              )}
              <span className="text-xs font-semibold text-brand-400">{t.category}</span>
              <span className="text-slate-500 text-xs">•</span>
              <span className="text-xs text-slate-500">{t.timeAgo}</span>
            </div>

            <h3 className="text-base font-bold text-white hover:text-brand-300 transition-colors cursor-pointer">
              {t.title}
            </h3>

            <div className="flex items-center justify-between pt-2 text-xs text-slate-400">
              <span>Posted by <strong className="text-slate-200">{t.author}</strong></span>
              <div className="flex items-center gap-4">
                <span className="flex items-center gap-1 text-slate-400">
                  <ThumbsUp className="w-3.5 h-3.5" /> {t.likes}
                </span>
                <span className="flex items-center gap-1 text-slate-400">
                  <MessageCircle className="w-3.5 h-3.5" /> {t.replies} replies
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
