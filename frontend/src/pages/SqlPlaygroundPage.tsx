import React from 'react';
import { SqlPlayground } from '../components/tools/SqlPlayground';

export const SqlPlaygroundPage: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-6">
      <div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Interactive SQL Sandbox</h1>
        <p className="text-xs text-slate-400 mt-1">Execute PostgreSQL & SQLite queries directly against live database tables</p>
      </div>
      <SqlPlayground />
    </div>
  );
};
