import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCartStore } from '../store/cartStore';
import { useAuthStore } from '../store/authStore';
import { apiClient } from '../api/client';
import { CreditCard, ShieldCheck, CheckCircle, ArrowRight, Lock, Loader2 } from 'lucide-react';
import { Button } from '../components/common/Button';

export const CheckoutPage: React.FC = () => {
  const { cart, clearCart } = useCartStore();
  const { user } = useAuthStore();
  const navigate = useNavigate();

  const [paymentMethod, setPaymentMethod] = useState('mock_gateway');
  const [isProcessing, setIsProcessing] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  if (!cart || cart.items.length === 0) {
    navigate('/cart');
    return null;
  }

  const handleCompletePayment = async () => {
    setIsProcessing(true);
    setErrorMessage(null);
    try {
      // 1. Create order
      const orderRes = await apiClient.post('/orders/checkout', {
        coupon_code: cart.applied_coupon || undefined,
        payment_method: paymentMethod
      });
      const orderId = orderRes.data.id;
      const orderNumber = orderRes.data.order_number;

      // 2. Initiate Payment
      const initRes = await apiClient.post('/payments/initiate', {
        order_id: orderId,
        payment_method: paymentMethod
      });
      const transactionId = initRes.data.transaction_id;

      // 3. Verify Payment
      await apiClient.post('/payments/verify', {
        transaction_id: transactionId,
        order_id: orderId
      });

      // 4. Success -> redirect
      navigate(`/order-success/${orderNumber}`);
    } catch (err: any) {
      setErrorMessage(err.response?.data?.detail || 'Payment processing failed. Please try again.');
      setIsProcessing(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-12 space-y-8">
      <div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Complete Your Order</h1>
        <p className="text-xs text-slate-400 mt-1">Review items and select payment method</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Payment Methods */}
        <div className="md:col-span-2 space-y-6">
          {/* Account info */}
          <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-2">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Customer Information</h4>
            <p className="text-sm font-semibold text-white">{user?.full_name} ({user?.email})</p>
          </div>

          {/* Payment selection */}
          <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-4">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Payment Method</h4>

            <div className="space-y-3">
              <label className="flex items-center justify-between p-4 rounded-xl border border-brand-500/40 bg-brand-500/5 cursor-pointer">
                <div className="flex items-center gap-3">
                  <input type="radio" checked readOnly className="text-brand-500" />
                  <div>
                    <span className="text-sm font-bold text-white block">Instant Sandbox Gateway (Test Mode)</span>
                    <span className="text-xs text-slate-400">Simulate successful card & PayPal transactions</span>
                  </div>
                </div>
                <CreditCard className="w-5 h-5 text-brand-400" />
              </label>
            </div>
          </div>

          {errorMessage && (
            <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs font-medium">
              {errorMessage}
            </div>
          )}
        </div>

        {/* Checkout Summary Card */}
        <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-4 shadow-xl">
          <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Order Summary</h4>
          <div className="space-y-2 text-xs text-slate-300">
            <div className="flex justify-between">
              <span>Items ({cart.item_count})</span>
              <span>${cart.subtotal.toFixed(2)}</span>
            </div>
            {cart.discount > 0 && (
              <div className="flex justify-between text-emerald-400 font-semibold">
                <span>Discount</span>
                <span>-${cart.discount.toFixed(2)}</span>
              </div>
            )}
            <div className="flex justify-between">
              <span>Tax</span>
              <span>${cart.tax.toFixed(2)}</span>
            </div>
            <div className="flex justify-between text-base font-extrabold text-white pt-2 border-t border-slate-800">
              <span>Total</span>
              <span className="text-brand-400">${cart.total.toFixed(2)} USD</span>
            </div>
          </div>

          <Button
            size="lg"
            variant="primary"
            className="w-full font-bold"
            onClick={handleCompletePayment}
            isLoading={isProcessing}
            leftIcon={<Lock className="w-4 h-4" />}
          >
            Pay ${cart.total.toFixed(2)}
          </Button>

          <p className="text-[10px] text-slate-500 text-center">
            By completing this transaction, you agree to CodePulse Academy terms of service.
          </p>
        </div>
      </div>
    </div>
  );
};
