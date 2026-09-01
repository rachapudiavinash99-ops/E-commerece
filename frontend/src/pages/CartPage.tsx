import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useCartStore } from '../store/cartStore';
import { Trash2, ShoppingBag, ArrowRight, Tag, ShieldCheck, Sparkles } from 'lucide-react';
import { Button } from '../components/common/Button';
import { EmptyState } from '../components/common/EmptyState';

export const CartPage: React.FC = () => {
  const { cart, fetchCart, removeFromCart, applyCoupon, discountMessage, isLoading } = useCartStore();
  const [couponInput, setCouponInput] = useState('');
  const [couponError, setCouponError] = useState<string | null>(null);
  const [isApplyingCoupon, setIsApplyingCoupon] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    fetchCart();
  }, []);

  const handleApplyCoupon = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!couponInput.trim()) return;
    setIsApplyingCoupon(true);
    setCouponError(null);
    try {
      await applyCoupon(couponInput.trim());
    } catch (err: any) {
      setCouponError(err.message || 'Failed to apply coupon');
    } finally {
      setIsApplyingCoupon(false);
    }
  };

  if (!cart || cart.items.length === 0) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-20">
        <EmptyState
          icon={<ShoppingBag className="w-10 h-10 text-brand-400" />}
          title="Your Shopping Cart is Empty"
          description="Explore our coding catalog to find top-tier masterclasses in Python, React, and Distributed Systems."
          actionText="Browse Courses"
          onAction={() => navigate('/courses')}
        />
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      <div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Shopping Cart</h1>
        <p className="text-xs text-slate-400 mt-1">{cart.item_count} courses in your cart</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-10 items-start">
        {/* Cart Items List */}
        <div className="lg:col-span-2 space-y-4">
          {cart.items.map((item) => (
            <div
              key={item.id}
              className="flex flex-col sm:flex-row items-start sm:items-center justify-between p-4 sm:p-5 rounded-2xl bg-slate-900/60 border border-slate-800 gap-4"
            >
              <div className="flex items-center gap-4">
                <img
                  src={item.course.thumbnail_url || 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600'}
                  alt={item.course.title}
                  className="w-20 h-14 object-cover rounded-xl border border-slate-800 flex-shrink-0"
                />
                <div className="space-y-1">
                  <Link to={`/courses/${item.course.slug}`} className="font-bold text-sm text-slate-100 hover:text-brand-300 transition-colors line-clamp-1">
                    {item.course.title}
                  </Link>
                  <p className="text-xs text-slate-400">By {item.course.instructor?.full_name || 'CodePulse Faculty'}</p>
                </div>
              </div>

              <div className="flex items-center justify-between w-full sm:w-auto sm:gap-6 border-t sm:border-t-0 border-slate-800/80 pt-3 sm:pt-0">
                <div className="text-right">
                  <div className="text-base font-black text-white">
                    ${item.course.discount_price !== undefined && item.course.discount_price !== null ? item.course.discount_price.toFixed(2) : item.course.price.toFixed(2)}
                  </div>
                  {item.course.discount_price !== undefined && item.course.discount_price !== null && item.course.discount_price < item.course.price && (
                    <span className="text-xs text-slate-500 line-through">
                      ${item.course.price.toFixed(2)}
                    </span>
                  )}
                </div>

                <button
                  onClick={() => removeFromCart(item.course_id)}
                  className="p-2 text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-lg transition-colors"
                  title="Remove"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Order Summary & Coupon Card */}
        <div className="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-6 shadow-2xl">
          <h3 className="text-lg font-bold text-white tracking-tight">Order Summary</h3>

          {/* Coupon Input */}
          <form onSubmit={handleApplyCoupon} className="space-y-2">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Tag className="w-3.5 h-3.5 text-brand-400" />
              <span>Promotional Coupon</span>
            </label>
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="e.g. CODEPULSE50"
                value={couponInput}
                onChange={(e) => setCouponInput(e.target.value.toUpperCase())}
                className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-white uppercase focus:outline-none focus:border-brand-500"
              />
              <Button size="sm" variant="secondary" type="submit" isLoading={isApplyingCoupon}>
                Apply
              </Button>
            </div>
            {discountMessage && <p className="text-xs text-emerald-400 font-semibold">{discountMessage}</p>}
            {couponError && <p className="text-xs text-rose-400 font-medium">{couponError}</p>}
          </form>

          {/* Calculation Breakdown */}
          <div className="space-y-2.5 pt-4 border-t border-slate-800 text-xs">
            <div className="flex justify-between text-slate-300">
              <span>Original Subtotal</span>
              <span>${cart.subtotal.toFixed(2)}</span>
            </div>

            {cart.discount > 0 && (
              <div className="flex justify-between text-emerald-400 font-semibold">
                <span>Coupon Discount</span>
                <span>-${cart.discount.toFixed(2)}</span>
              </div>
            )}

            <div className="flex justify-between text-slate-300">
              <span>Estimated Tax (5%)</span>
              <span>${cart.tax.toFixed(2)}</span>
            </div>

            <div className="flex justify-between text-base font-extrabold text-white pt-3 border-t border-slate-800">
              <span>Total Due</span>
              <span className="text-brand-400">${cart.total.toFixed(2)} USD</span>
            </div>
          </div>

          <Button
            size="lg"
            variant="primary"
            className="w-full font-bold shadow-lg shadow-brand-500/20"
            onClick={() => navigate('/checkout')}
            rightIcon={<ArrowRight className="w-4 h-4" />}
          >
            Proceed to Checkout
          </Button>

          <div className="flex items-center justify-center gap-2 text-[11px] text-slate-500 text-center">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <span>Guaranteed Safe & Secure Checkout</span>
          </div>
        </div>
      </div>
    </div>
  );
};
