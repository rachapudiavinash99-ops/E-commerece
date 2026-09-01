import React, { useState } from 'react';
import { Copy, Check } from 'lucide-react';

interface CodeBlockProps {
  code: string;
  language?: string;
  title?: string;
  showLineNumbers?: boolean;
}

export const CodeBlock: React.FC<CodeBlockProps> = ({
  code,
  language = 'python',
  title,
  showLineNumbers = true
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const lines = code.trim().split('\n');

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-950 overflow-hidden font-mono text-xs shadow-2xl">
      <div className="bg-slate-900/80 px-4 py-2.5 border-b border-slate-800 flex items-center justify-between text-slate-400">
        <span className="font-semibold text-[11px] text-slate-300">{title || language}</span>
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
        >
          {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
          <span className="text-[10px]">{copied ? 'Copied' : 'Copy Code'}</span>
        </button>
      </div>

      <div className="p-4 overflow-x-auto leading-relaxed flex">
        {showLineNumbers && (
          <div className="select-none pr-4 text-slate-600 text-right font-mono">
            {lines.map((_, i) => (
              <div key={i}>{i + 1}</div>
            ))}
          </div>
        )}
        <pre className="text-slate-200 flex-1">{code.trim()}</pre>
      </div>
    </div>
  );
};
