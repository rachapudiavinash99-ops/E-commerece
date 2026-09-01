import React, { useState, useMemo } from 'react';
import { Terminal, Check, Sparkles, Copy } from 'lucide-react';
import { Input } from '../common/Input';
import { Button } from '../common/Button';

export const RegexTester: React.FC = () => {
  const [pattern, setPattern] = useState('([A-Z0-9._%+-]+)@([A-Z0-9.-]+\.[A-Z]{2,})');
  const [flags, setFlags] = useState('gi');
  const [testString, setTestString] = useState(`Contact student@codepulse.io or instructor@python.org for course inquiries.
Admin support is available at admin@enterprise-academy.com.`);

  const matchResults = useMemo(() => {
    try {
      const regex = new RegExp(pattern, flags);
      const matches = Array.from(testString.matchAll(regex));
      return { matches, error: null };
    } catch (err: any) {
      return { matches: [], error: err.message };
    }
  }, [pattern, flags, testString]);

  return (
    <div className="space-y-6">
      <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6 shadow-2xl">
        <h3 className="text-lg font-bold text-white tracking-tight">Interactive Regular Expression Tester</h3>

        <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
          <div className="sm:col-span-3">
            <Input
              label="Regular Expression Pattern"
              value={pattern}
              onChange={(e) => setPattern(e.target.value)}
              placeholder="e.g. ^[a-zA-Z0-9]+$"
            />
          </div>
          <div>
            <Input
              label="Flags (g, i, m, s)"
              value={flags}
              onChange={(e) => setFlags(e.target.value)}
              placeholder="gi"
            />
          </div>
        </div>

        <div className="space-y-1.5">
          <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Test String</label>
          <textarea
            rows={5}
            value={testString}
            onChange={(e) => setTestString(e.target.value)}
            className="w-full bg-slate-950 border border-slate-800 rounded-xl p-4 font-mono text-xs text-slate-100 focus:outline-none focus:border-brand-500 leading-relaxed"
          />
        </div>

        {/* Results */}
        {matchResults.error ? (
          <p className="text-xs text-rose-400 font-mono">Regex Error: {matchResults.error}</p>
        ) : (
          <div className="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between text-xs text-slate-400 font-mono">
              <span className="text-emerald-400 font-bold">{matchResults.matches.length} Matches Found</span>
            </div>
            <div className="space-y-1">
              {matchResults.matches.map((m, idx) => (
                <div key={idx} className="p-2 rounded bg-slate-900 font-mono text-xs text-brand-300 flex items-center justify-between">
                  <span>Match #{idx + 1}: <strong>{m[0]}</strong></span>
                  <span className="text-slate-500 text-[11px]">Index: {m.index}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
