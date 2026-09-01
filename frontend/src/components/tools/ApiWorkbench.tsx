import React, { useState } from 'react';
import { Send, Globe, Play, Sparkles, CheckCircle2 } from 'lucide-react';
import { Button } from '../common/Button';

export const ApiWorkbench: React.FC = () => {
  const [method, setMethod] = useState<'GET' | 'POST' | 'PUT' | 'DELETE'>('GET');
  const [url, setUrl] = useState('/api/courses?page_size=2');
  const [headers, setHeaders] = useState('{\n  "Content-Type": "application/json"\n}');
  const [response, setResponse] = useState<string>(`{
  "status": 200,
  "data": {
    "total": 8,
    "page": 1,
    "items": [
      {
        "id": 1,
        "title": "Python 3.12 Masterclass: Fundamentals to Architecture",
        "price": 89.99,
        "rating": 4.95
      }
    ]
  },
  "execution_time_ms": 14.8
}`);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendRequest = () => {
    setIsLoading(true);
    setTimeout(() => {
      setResponse(JSON.stringify({
        status: 200,
        data: {
          items: [
            { id: 1, title: "Python 3.12 Masterclass", price: 89.99 },
            { id: 2, title: "FastAPI Microservices", price: 79.99 }
          ],
          total: 2
        },
        execution_time_ms: 12.3
      }, null, 2));
      setIsLoading(false);
    }, 400);
  };

  return (
    <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6 shadow-2xl">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold text-white tracking-tight flex items-center gap-2">
          <Globe className="w-5 h-5 text-brand-400" />
          <span>API Request Workbench & Live Inspector</span>
        </h3>
      </div>

      {/* URL bar */}
      <div className="flex gap-2">
        <select
          value={method}
          onChange={(e: any) => setMethod(e.target.value)}
          className="bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs font-bold text-brand-400 focus:outline-none"
        >
          <option value="GET">GET</option>
          <option value="POST">POST</option>
          <option value="PUT">PUT</option>
          <option value="DELETE">DELETE</option>
        </select>

        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-xs font-mono text-white focus:outline-none focus:border-brand-500"
        />

        <Button variant="primary" onClick={handleSendRequest} isLoading={isLoading} rightIcon={<Send className="w-3.5 h-3.5" />}>
          Send
        </Button>
      </div>

      {/* Response visualizer */}
      <div className="space-y-2">
        <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">JSON Response Payload</span>
        <pre className="p-4 rounded-2xl bg-slate-950 border border-slate-800 font-mono text-xs text-emerald-400 overflow-x-auto leading-relaxed">
          {response}
        </pre>
      </div>
    </div>
  );
};
