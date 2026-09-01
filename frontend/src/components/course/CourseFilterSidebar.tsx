import React from 'react';
import { Category, Topic } from '../../types';
import { Star, Filter, RotateCcw } from 'lucide-react';

interface FilterSidebarProps {
  categories: Category[];
  selectedCategory: number | null;
  onSelectCategory: (id: number | null) => void;
  selectedTopic: number | null;
  onSelectTopic: (id: number | null) => void;
  selectedLevel: string | null;
  onSelectLevel: (level: string | null) => void;
  minRating: number | null;
  onSelectRating: (rating: number | null) => void;
  onReset: () => void;
}

export const CourseFilterSidebar: React.FC<FilterSidebarProps> = ({
  categories,
  selectedCategory,
  onSelectCategory,
  selectedTopic,
  onSelectTopic,
  selectedLevel,
  onSelectLevel,
  minRating,
  onSelectRating,
  onReset,
}) => {
  const levels = [
    { label: 'All Levels', value: 'all_levels' },
    { label: 'Beginner', value: 'beginner' },
    { label: 'Intermediate', value: 'intermediate' },
    { label: 'Advanced', value: 'advanced' },
  ];

  const ratings = [4.5, 4.0, 3.5, 3.0];

  return (
    <aside className="w-full lg:w-64 space-y-6 bg-slate-900/40 p-5 rounded-2xl border border-slate-800">
      <div className="flex items-center justify-between pb-4 border-b border-slate-800">
        <div className="flex items-center gap-2 font-bold text-sm text-slate-100">
          <Filter className="w-4 h-4 text-brand-400" />
          <span>Filter Courses</span>
        </div>
        <button
          onClick={onReset}
          className="text-xs text-slate-400 hover:text-brand-400 flex items-center gap-1 transition-colors"
        >
          <RotateCcw className="w-3 h-3" />
          Reset
        </button>
      </div>

      {/* Category Section */}
      <div className="space-y-2.5">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Categories</h4>
        <div className="space-y-1">
          <button
            onClick={() => onSelectCategory(null)}
            className={`w-full text-left px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
              selectedCategory === null ? 'bg-brand-500/20 text-brand-300 font-semibold' : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
            }`}
          >
            All Categories
          </button>
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`w-full text-left px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                selectedCategory === cat.id ? 'bg-brand-500/20 text-brand-300 font-semibold' : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
              }`}
            >
              {cat.name}
            </button>
          ))}
        </div>
      </div>

      {/* Difficulty Level */}
      <div className="space-y-2.5 pt-4 border-t border-slate-800">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Difficulty Level</h4>
        <div className="space-y-1">
          {levels.map((lvl) => (
            <button
              key={lvl.value}
              onClick={() => onSelectLevel(selectedLevel === lvl.value ? null : lvl.value)}
              className={`w-full text-left px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                selectedLevel === lvl.value ? 'bg-brand-500/20 text-brand-300 font-semibold' : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
              }`}
            >
              {lvl.label}
            </button>
          ))}
        </div>
      </div>

      {/* Minimum Rating */}
      <div className="space-y-2.5 pt-4 border-t border-slate-800">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Minimum Rating</h4>
        <div className="space-y-1">
          {ratings.map((rate) => (
            <button
              key={rate}
              onClick={() => onSelectRating(minRating === rate ? null : rate)}
              className={`w-full flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                minRating === rate ? 'bg-amber-500/10 text-amber-300 font-semibold' : 'text-slate-400 hover:bg-slate-800/60 hover:text-slate-200'
              }`}
            >
              <div className="flex items-center text-amber-400">
                <Star className="w-3.5 h-3.5 fill-amber-400" />
              </div>
              <span>{rate} & above</span>
            </button>
          ))}
        </div>
      </div>
    </aside>
  );
};
