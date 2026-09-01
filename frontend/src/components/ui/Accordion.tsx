import React, { useState } from 'react';
import { ChevronDown } from 'lucide-react';

interface AccordionItem {
  id: string;
  title: string;
  content: React.ReactNode;
}

interface AccordionProps {
  items: AccordionItem[];
  allowMultiple?: boolean;
}

export const Accordion: React.FC<AccordionProps> = ({ items, allowMultiple = false }) => {
  const [openIds, setOpenIds] = useState<string[]>([items[0]?.id || '']);

  const toggle = (id: string) => {
    if (allowMultiple) {
      setOpenIds(openIds.includes(id) ? openIds.filter((i) => i !== id) : [...openIds, id]);
    } else {
      setOpenIds(openIds.includes(id) ? [] : [id]);
    }
  };

  return (
    <div className="space-y-3">
      {items.map((item) => {
        const isOpen = openIds.includes(item.id);
        return (
          <div key={item.id} className="rounded-2xl bg-slate-900 border border-slate-800 overflow-hidden transition-all">
            <button
              onClick={() => toggle(item.id)}
              className="w-full flex items-center justify-between p-4 text-left font-bold text-sm text-slate-200 hover:text-white transition-colors"
            >
              <span>{item.title}</span>
              <ChevronDown className={`w-4 h-4 text-slate-400 transition-transform duration-200 ${isOpen ? 'rotate-180 text-brand-400' : ''}`} />
            </button>
            {isOpen && (
              <div className="px-4 pb-4 pt-1 text-xs text-slate-300 border-t border-slate-850 leading-relaxed animate-in fade-in duration-150">
                {item.content}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};
