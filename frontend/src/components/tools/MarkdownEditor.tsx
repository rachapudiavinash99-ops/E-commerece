import React, { useState } from 'react';
import { FileText, Eye, Edit3, Sparkles } from 'lucide-react';

export const MarkdownEditor: React.FC = () => {
  const [markdown, setMarkdown] = useState(`# System Architecture Specification

## Overview
This specification details the **CodePulse Academy** architectural patterns.

### Key Components
1. **API Gateway**: FastAPI with rate limiting and JWT auth.
2. **Persistence**: PostgreSQL + SQLAlchemy 2.0 ORM.
3. **Execution Sandbox**: Python 3.12 AST AST-safe evaluator.

\`\`\`python
def evaluate_code(source: str) -> dict:
    return {"status": "passed", "score": 100}
\`\`\`
`);

  const [activeTab, setActiveTab] = useState<'write' | 'preview' | 'split'>('split');

  return (
    <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-4 shadow-2xl">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold text-white tracking-tight flex items-center gap-2">
          <FileText className="w-5 h-5 text-brand-400" />
          <span>Interactive Markdown & Documentation Studio</span>
        </h3>

        <div className="flex gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs">
          <button
            onClick={() => setActiveTab('write')}
            className={`px-3 py-1 rounded-lg ${activeTab === 'write' ? 'bg-brand-500 text-white' : 'text-slate-400'}`}
          >
            Write
          </button>
          <button
            onClick={() => setActiveTab('preview')}
            className={`px-3 py-1 rounded-lg ${activeTab === 'preview' ? 'bg-brand-500 text-white' : 'text-slate-400'}`}
          >
            Preview
          </button>
          <button
            onClick={() => setActiveTab('split')}
            className={`px-3 py-1 rounded-lg ${activeTab === 'split' ? 'bg-brand-500 text-white' : 'text-slate-400'}`}
          >
            Split View
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {(activeTab === 'write' || activeTab === 'split') && (
          <textarea
            rows={12}
            value={markdown}
            onChange={(e) => setMarkdown(e.target.value)}
            className="w-full bg-slate-950 border border-slate-800 rounded-2xl p-4 font-mono text-xs text-slate-100 focus:outline-none focus:border-brand-500 leading-relaxed"
          />
        )}

        {(activeTab === 'preview' || activeTab === 'split') && (
          <div className="p-4 rounded-2xl bg-slate-950 border border-slate-800 prose prose-invert max-w-none text-xs text-slate-300 overflow-y-auto max-h-[300px] whitespace-pre-line leading-relaxed">
            {markdown}
          </div>
        )}
      </div>
    </div>
  );
};
