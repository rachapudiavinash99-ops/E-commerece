import React, { useState } from 'react';
import { Database, Play, RotateCcw, Table as TableIcon, CheckCircle2, AlertCircle, Sparkles } from 'lucide-react';
import { Button } from '../common/Button';

interface SqlQueryResult {
  columns: string[];
  rows: any[][];
  executionTimeMs: number;
  rowCount: number;
}

export const SqlPlayground: React.FC = () => {
  const [query, setQuery] = useState(`-- Query courses with high ratings and student enrollments
SELECT 
    c.id,
    c.title,
    c.price,
    c.average_rating,
    c.student_count,
    t.name AS topic_name
FROM courses c
JOIN topics t ON c.topic_id = t.id
WHERE c.average_rating >= 4.8
ORDER BY c.student_count DESC
LIMIT 10;`);

  const [result, setResult] = useState<SqlQueryResult | null>({
    columns: ['id', 'title', 'price', 'average_rating', 'student_count', 'topic_name'],
    rows: [
      [1, 'Python 3.12 Masterclass: Architecture & Concurrency', 89.99, 4.95, 3420, 'Python Architecture'],
      [2, 'FastAPI Microservices & Distributed Event Systems', 79.99, 4.92, 2810, 'FastAPI Microservices'],
      [3, 'Data Structures & Algorithms: Interview Playbook', 69.99, 4.88, 4150, 'Algorithms & DSA'],
      [4, 'React 18 & TypeScript Enterprise Design Systems', 74.99, 4.85, 2390, 'React & TypeScript']
    ],
    executionTimeMs: 4.2,
    rowCount: 4
  });

  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRunQuery = () => {
    setIsRunning(true);
    setError(null);
    setTimeout(() => {
      if (query.toLowerCase().includes('syntax error')) {
        setError('SQL Syntax Error: unexpected token near line 1');
        setResult(null);
      } else {
        setResult({
          columns: ['id', 'title', 'price', 'average_rating', 'student_count', 'topic_name'],
          rows: [
            [1, 'Python 3.12 Masterclass: Architecture & Concurrency', 89.99, 4.95, 3420, 'Python Architecture'],
            [2, 'FastAPI Microservices & Distributed Event Systems', 79.99, 4.92, 2810, 'FastAPI Microservices'],
            [3, 'Data Structures & Algorithms: Interview Playbook', 69.99, 4.88, 4150, 'Algorithms & DSA'],
            [4, 'React 18 & TypeScript Enterprise Design Systems', 74.99, 4.85, 2390, 'React & TypeScript']
          ],
          executionTimeMs: Number((Math.random() * 8 + 2).toFixed(1)),
          rowCount: 4
        });
      }
      setIsRunning(false);
    }, 300);
  };

  return (
    <div className="space-y-6">
      {/* Editor Box */}
      <div className="rounded-2xl bg-slate-900 border border-slate-800 overflow-hidden shadow-2xl">
        <div className="bg-slate-950 px-4 py-3 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-300">
            <Database className="w-4 h-4 text-brand-400" />
            <span>Interactive SQL Playground (PostgreSQL / SQLite Sandbox)</span>
          </div>
          <div className="flex items-center gap-2">
            <Button
              size="sm"
              variant="ghost"
              onClick={() => setQuery('')}
              leftIcon={<RotateCcw className="w-3.5 h-3.5" />}
            >
              Clear
            </Button>
            <Button
              size="sm"
              variant="primary"
              onClick={handleRunQuery}
              isLoading={isRunning}
              leftIcon={<Play className="w-3.5 h-3.5" />}
            >
              Execute SQL
            </Button>
          </div>
        </div>

        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          rows={7}
          className="w-full bg-slate-900 p-4 font-mono text-xs text-slate-100 focus:outline-none resize-none leading-relaxed"
          spellCheck={false}
        />
      </div>

      {/* Query Results */}
      {error && (
        <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs flex items-center gap-2">
          <AlertCircle className="w-4 h-4" />
          <span>{error}</span>
        </div>
      )}

      {result && (
        <div className="rounded-2xl bg-slate-900 border border-slate-800 overflow-hidden shadow-xl space-y-2">
          <div className="p-4 bg-slate-950/60 border-b border-slate-800 flex items-center justify-between text-xs text-slate-400 font-mono">
            <span className="flex items-center gap-1.5 text-emerald-400 font-semibold">
              <CheckCircle2 className="w-4 h-4" />
              Query returned {result.rowCount} rows
            </span>
            <span>Execution time: <strong className="text-white">{result.executionTimeMs}ms</strong></span>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono text-slate-200">
              <thead className="bg-slate-950 text-slate-400 uppercase font-semibold text-[10px]">
                <tr>
                  {result.columns.map((col, idx) => (
                    <th key={idx} className="p-3.5 border-b border-slate-800">{col}</th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-850">
                {result.rows.map((row, rowIdx) => (
                  <tr key={rowIdx} className="hover:bg-slate-850/60">
                    {row.map((cell, cellIdx) => (
                      <td key={cellIdx} className="p-3.5">{String(cell)}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
