import React from 'react';
import { Map, ArrowRight, Code, Server, Layers, Cloud, ShieldCheck } from 'lucide-react';
import { Button } from '../components/common/Button';
import { useNavigate } from 'react-router-dom';

export const LearningRoadmapsPage: React.FC = () => {
  const navigate = useNavigate();

  const roadmaps = [
    {
      title: 'Python Software Architect',
      desc: 'From Python foundations to metaclasses, asyncio concurrency, and distributed worker patterns.',
      icon: <Code className="w-6 h-6 text-brand-400" />,
      coursesCount: 4,
      estimatedWeeks: 12
    },
    {
      title: 'Full-Stack React & FastAPI Engineer',
      desc: 'Master end-to-end API design, PostgreSQL transactional ORMs, React 18 hooks, and state stores.',
      icon: <Layers className="w-6 h-6 text-cyan-400" />,
      coursesCount: 5,
      estimatedWeeks: 16
    },
    {
      title: 'Distributed Systems & Cloud DevOps Lead',
      desc: 'Master Raft consensus, Docker containers, Kubernetes orchestration, and Kafka stream processing.',
      icon: <Cloud className="w-6 h-6 text-purple-400" />,
      coursesCount: 4,
      estimatedWeeks: 14
    },
    {
      title: 'Data Structures & Algorithmic Interview Master',
      desc: '150+ LeetCode patterns across Graphs, Dynamic Programming, Trees, Heaps, and Backtracking.',
      icon: <Server className="w-6 h-6 text-amber-400" />,
      coursesCount: 3,
      estimatedWeeks: 10
    }
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-12">
      <div className="text-center space-y-4 max-w-3xl mx-auto">
        <div className="inline-flex p-3 bg-brand-500/10 rounded-2xl text-brand-400 border border-brand-500/20">
          <Map className="w-6 h-6" />
        </div>
        <h1 className="text-4xl font-extrabold text-white tracking-tight">Curated Engineering Roadmaps</h1>
        <p className="text-sm text-slate-400">
          Structured step-by-step career tracks designed to take you from junior to Staff Software Engineer.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {roadmaps.map((r, idx) => (
          <div
            key={idx}
            className="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 hover:border-slate-700 transition-all space-y-6 shadow-xl"
          >
            <div className="flex items-center gap-4">
              <div className="p-3 bg-slate-950 rounded-2xl border border-slate-800">
                {r.icon}
              </div>
              <div>
                <h3 className="text-lg font-bold text-white">{r.title}</h3>
                <span className="text-xs text-slate-400">{r.coursesCount} Courses • {r.estimatedWeeks} Weeks</span>
              </div>
            </div>

            <p className="text-xs text-slate-300 leading-relaxed">{r.desc}</p>

            <Button
              variant="outline"
              size="sm"
              onClick={() => navigate('/courses')}
              rightIcon={<ArrowRight className="w-4 h-4" />}
            >
              View Roadmap Curriculum
            </Button>
          </div>
        ))}
      </div>
    </div>
  );
};
