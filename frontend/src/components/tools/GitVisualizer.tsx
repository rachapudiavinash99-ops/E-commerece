import React, { useState } from 'react';
import { GitBranch, GitCommit, GitMerge, Check, Plus } from 'lucide-react';
import { Button } from '../common/Button';

interface CommitNode {
  id: string;
  message: string;
  branch: string;
  author: string;
  isMerge?: boolean;
}

const initialCommits: CommitNode[] = [
  { id: '2d779f0', message: 'chore: initialize full-stack architecture', branch: 'main', author: 'Avinash Rachapudi' },
  { id: 'ba28628', message: 'feat(database): implement 22+ SQLAlchemy models', branch: 'main', author: 'Avinash Rachapudi' },
  { id: 'aac3654', message: 'feat(schemas): implement Pydantic v2 validation', branch: 'main', author: 'Avinash Rachapudi' },
  { id: '9e5750e', message: 'feat(api): implement 20+ REST endpoints', branch: 'feature/api', author: 'Avinash Rachapudi' },
  { id: '7fbe320', message: 'test(backend): Pytest automated test suite', branch: 'feature/tests', author: 'Avinash Rachapudi' },
  { id: '0643143', message: 'feat(learning): interactive student code IDE', branch: 'main', author: 'Avinash Rachapudi', isMerge: true }
];

export const GitVisualizer: React.FC = () => {
  const [commits, setCommits] = useState<CommitNode[]>(initialCommits);
  const [newMsg, setNewMsg] = useState('');

  const handleAddCommit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newMsg.trim()) return;
    const newId = Math.random().toString(16).substring(2, 9);
    setCommits([
      ...commits,
      { id: newId, message: newMsg.trim(), branch: 'main', author: 'Avinash Rachapudi' }
    ]);
    setNewMsg('');
  };

  return (
    <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6 shadow-2xl">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-lg font-bold text-white tracking-tight flex items-center gap-2">
            <GitBranch className="w-5 h-5 text-brand-400" />
            <span>Interactive Git Branch & Commit DAG Tree</span>
          </h3>
          <p className="text-xs text-slate-400">Visual commit history graph with merge nodes</p>
        </div>
      </div>

      <form onSubmit={handleAddCommit} className="flex gap-2">
        <input
          type="text"
          placeholder="New commit message (e.g. feat(auth): add OAuth2 provider)..."
          value={newMsg}
          onChange={(e) => setNewMsg(e.target.value)}
          className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-xs text-white focus:outline-none focus:border-brand-500"
        />
        <Button size="sm" variant="primary" type="submit" leftIcon={<Plus className="w-3.5 h-3.5" />}>
          Commit
        </Button>
      </form>

      {/* DAG Node Graph */}
      <div className="space-y-3 pt-2">
        {commits.map((c, idx) => (
          <div
            key={c.id}
            className="flex items-center justify-between p-3.5 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs hover:border-brand-500/40 transition-colors"
          >
            <div className="flex items-center gap-3">
              <div className={`p-1.5 rounded-lg ${c.isMerge ? 'bg-purple-500/20 text-purple-400' : 'bg-brand-500/20 text-brand-400'}`}>
                {c.isMerge ? <GitMerge className="w-4 h-4" /> : <GitCommit className="w-4 h-4" />}
              </div>
              <div>
                <span className="font-bold text-white">{c.message}</span>
                <div className="flex items-center gap-2 text-[10px] text-slate-500 pt-0.5">
                  <span>Branch: <strong className="text-brand-400">{c.branch}</strong></span>
                  <span>•</span>
                  <span>{c.author}</span>
                </div>
              </div>
            </div>
            <span className="text-[11px] font-bold text-amber-400">{c.id}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
