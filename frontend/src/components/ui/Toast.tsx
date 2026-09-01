import React from 'react';
import { CheckCircle2, AlertTriangle, XCircle, Info, X } from 'lucide-react';

export type ToastType = 'success' | 'error' | 'warning' | 'info';

export interface ToastProps {
  id: string;
  type: ToastType;
  title: string;
  message?: string;
  onClose: (id: string) => void;
}

export const Toast: React.FC<ToastProps> = ({ id, type, title, message, onClose }) => {
  const icons = {
    success: <CheckCircle2 className="w-5 h-5 text-emerald-400 flex-shrink-0" />,
    error: <XCircle className="w-5 h-5 text-rose-400 flex-shrink-0" />,
    warning: <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0" />,
    info: <Info className="w-5 h-5 text-brand-400 flex-shrink-0" />
  };

  const borders = {
    success: 'border-emerald-500/30 bg-emerald-950/40 text-emerald-100',
    error: 'border-rose-500/30 bg-rose-950/40 text-rose-100',
    warning: 'border-amber-500/30 bg-amber-950/40 text-amber-100',
    info: 'border-brand-500/30 bg-brand-950/40 text-brand-100'
  };

  return (
    <div className={`flex items-start gap-3 p-4 rounded-2xl border ${borders[type]} shadow-2xl backdrop-blur-md max-w-sm w-full animate-in slide-in-from-top duration-200`}>
      {icons[type]}
      <div className="flex-1 space-y-0.5">
        <h4 className="text-xs font-bold leading-none">{title}</h4>
        {message && <p className="text-[11px] opacity-80 leading-tight">{message}</p>}
      </div>
      <button onClick={() => onClose(id)} className="p-0.5 opacity-60 hover:opacity-100 transition-opacity">
        <X className="w-4 h-4" />
      </button>
    </div>
  );
};
