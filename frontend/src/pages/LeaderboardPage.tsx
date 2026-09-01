import React from 'react';
import { Trophy, Award, Zap, Star, ShieldCheck } from 'lucide-react';
import { Badge } from '../components/common/Badge';

export const LeaderboardPage: React.FC = () => {
  const leaders = [
    { rank: 1, name: 'Alex Rivera', points: 4850, tasksSolved: 142, certs: 8, badge: 'Staff Master' },
    { rank: 2, name: 'Elena Rostova', points: 4210, tasksSolved: 128, certs: 7, badge: 'Algorithm Lead' },
    { rank: 3, name: 'David Kim', points: 3950, tasksSolved: 115, certs: 6, badge: 'Senior Architect' },
    { rank: 4, name: 'Sarah Connor', points: 3620, tasksSolved: 104, certs: 5, badge: 'Full-Stack Lead' },
    { rank: 5, name: 'Michael Chang', points: 3180, tasksSolved: 92, certs: 4, badge: 'Cloud Developer' }
  ];

  return (
    <div className="max-w-4xl mx-auto px-4 py-12 space-y-8">
      <div className="text-center space-y-3">
        <div className="inline-flex p-3 bg-amber-500/10 rounded-2xl text-amber-400 border border-amber-500/20">
          <Trophy className="w-8 h-8" />
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Global Coding Leaderboard</h1>
        <p className="text-xs text-slate-400">Top ranking developers based on verified code sandbox task solutions</p>
      </div>

      <div className="rounded-3xl border border-slate-800 bg-slate-900 overflow-hidden shadow-2xl">
        <table className="w-full text-left text-xs text-slate-300">
          <thead className="bg-slate-950 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
            <tr>
              <th className="p-4">Rank</th>
              <th className="p-4">Developer</th>
              <th className="p-4">Points</th>
              <th className="p-4">Tasks Solved</th>
              <th className="p-4">Certificates</th>
              <th className="p-4">Tier</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-850">
            {leaders.map((u) => (
              <tr key={u.rank} className="hover:bg-slate-850/50 transition-colors">
                <td className="p-4 font-black text-sm">
                  {u.rank === 1 ? '🥇 1' : u.rank === 2 ? '🥈 2' : u.rank === 3 ? '🥉 3' : `#${u.rank}`}
                </td>
                <td className="p-4 font-bold text-white">{u.name}</td>
                <td className="p-4 font-extrabold text-amber-400">{u.points.toLocaleString()} pts</td>
                <td className="p-4">{u.tasksSolved} tasks</td>
                <td className="p-4">{u.certs} verified</td>
                <td className="p-4"><Badge variant="brand">{u.badge}</Badge></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
