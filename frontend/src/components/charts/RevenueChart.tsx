import React from 'react';

interface RevenueDataPoint {
  month: string;
  revenue: number;
  students: number;
}

const mockData: RevenueDataPoint[] = [
  { month: 'Jan', revenue: 12400, students: 210 },
  { month: 'Feb', revenue: 15800, students: 280 },
  { month: 'Mar', revenue: 22400, students: 390 },
  { month: 'Apr', revenue: 28900, students: 460 },
  { month: 'May', revenue: 34500, students: 580 },
  { month: 'Jun', revenue: 42100, students: 690 },
  { month: 'Jul', revenue: 48900, students: 780 },
  { month: 'Aug', revenue: 56200, students: 890 }
];

export const RevenueChart: React.FC = () => {
  const maxRevenue = Math.max(...mockData.map((d) => d.revenue));

  return (
    <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6 shadow-2xl">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-white tracking-tight">Platform Gross Revenue Trends</h3>
          <p className="text-xs text-slate-400">Monthly gross sales and active student enrollments</p>
        </div>
        <span className="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">
          +45.2% YoY
        </span>
      </div>

      {/* SVG Bar / Area Visualization */}
      <div className="h-48 flex items-end justify-between gap-3 pt-6">
        {mockData.map((item, idx) => {
          const heightPct = (item.revenue / maxRevenue) * 100;
          return (
            <div key={idx} className="flex-1 flex flex-col items-center gap-2 group">
              <div className="text-[10px] font-mono text-slate-400 opacity-0 group-hover:opacity-100 transition-opacity">
                ${(item.revenue / 1000).toFixed(1)}k
              </div>
              <div className="w-full bg-slate-950 rounded-lg h-36 flex items-end p-1">
                <div
                  className="w-full bg-gradient-to-t from-brand-600 to-cyan-400 rounded-md transition-all duration-500 group-hover:brightness-125"
                  style={{ height: `${heightPct}%` }}
                />
              </div>
              <span className="text-[11px] font-semibold text-slate-400">{item.month}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
