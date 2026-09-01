import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatWidgetProps {
  label: string;
  value: string | number;
  change?: string;
  isPositive?: boolean;
  icon: React.ReactNode;
}

export const StatWidget: React.FC<StatWidgetProps> = ({
  label,
  value,
  change,
  isPositive = true,
  icon
}) => {
  return (
    <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-3 shadow-xl">
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">{label}</span>
        <div className="p-2 rounded-xl bg-slate-950 border border-slate-800 text-brand-400">
          {icon}
        </div>
      </div>
      <div className="flex items-baseline justify-between">
        <div className="text-2xl font-black text-white">{value}</div>
        {change && (
          <span className={`text-xs font-bold ${isPositive ? 'text-emerald-400' : 'text-rose-400'}`}>
            {change}
          </span>
        )}
      </div>
    </div>
  );
};
