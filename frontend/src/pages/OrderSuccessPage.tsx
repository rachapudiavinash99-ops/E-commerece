import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { Order } from '../types';
import { apiClient } from '../api/client';
import { CheckCircle2, ArrowRight, BookOpen, ShieldCheck, Download } from 'lucide-react';
import { Button } from '../components/common/Button';

export const OrderSuccessPage: React.FC = () => {
  const { orderNumber } = useParams<{ orderNumber: string }>();
  const [order, setOrder] = useState<Order | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    if (!orderNumber) return;
    apiClient.get<Order>(`/orders/${orderNumber}`)
      .then((res) => setOrder(res.data))
      .catch(console.error)
      .finally(() => setIsLoading(false));
  }, [orderNumber]);

  return (
    <div className="max-w-3xl mx-auto px-4 py-16 text-center space-y-8">
      <div className="inline-flex p-4 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
        <CheckCircle2 className="w-12 h-12" />
      </div>

      <div className="space-y-2">
        <h1 className="text-3xl font-extrabold text-white tracking-tight">
          Payment Successful & Enrolled!
        </h1>
        <p className="text-sm text-slate-400">
          Order reference: <strong className="text-brand-400 font-mono">#{orderNumber}</strong>
        </p>
      </div>

      {order && (
        <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 text-left space-y-4 shadow-xl">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Purchased Courses</h3>
          <div className="divide-y divide-slate-800">
            {order.items.map((item) => (
              <div key={item.id} className="py-3 flex items-center justify-between text-xs">
                <span className="font-semibold text-white">{item.course.title}</span>
                <span className="font-bold text-slate-300">${item.price.toFixed(2)}</span>
              </div>
            ))}
          </div>
          <div className="flex justify-between pt-3 border-t border-slate-800 text-xs font-bold text-white">
            <span>Total Paid</span>
            <span className="text-emerald-400">${order.total.toFixed(2)} {order.currency}</span>
          </div>
        </div>
      )}

      <div className="flex flex-wrap items-center justify-center gap-4 pt-4">
        <Button
          size="lg"
          variant="primary"
          onClick={() => navigate('/student/dashboard')}
          rightIcon={<ArrowRight className="w-5 h-5" />}
        >
          Go to Student Learning Dashboard
        </Button>
      </div>
    </div>
  );
};
