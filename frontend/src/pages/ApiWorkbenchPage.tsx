import React from 'react';
import { ApiWorkbench } from '../components/tools/ApiWorkbench';
import { RegexTester } from '../components/tools/RegexTester';

export const ApiWorkbenchPage: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
      <div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Developer Tools & API Workbench</h1>
        <p className="text-xs text-slate-400 mt-1">Live HTTP request builder, response payload inspector, and regex tester</p>
      </div>
      <ApiWorkbench />
      <RegexTester />
    </div>
  );
};
