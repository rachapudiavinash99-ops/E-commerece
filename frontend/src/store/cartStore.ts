import { create } from 'zustand';
import { Cart } from '../types';
import { apiClient } from '../api/client';

interface CartState {
  cart: Cart | null;
  isLoading: boolean;
  couponCode: string;
  discountMessage: string | null;
  fetchCart: (coupon?: string) => Promise<void>;
  addToCart: (courseId: number) => Promise<void>;
  removeFromCart: (courseId: number) => Promise<void>;
  applyCoupon: (code: string) => Promise<void>;
  clearCart: () => Promise<void>;
}

export const useCartStore = create<CartState>((set, get) => ({
  cart: null,
  isLoading: false,
  couponCode: '',
  discountMessage: null,

  fetchCart: async (coupon) => {
    set({ isLoading: true });
    try {
      const code = coupon !== undefined ? coupon : get().couponCode;
      const res = await apiClient.get('/cart', { params: { coupon_code: code || undefined } });
      set({ cart: res.data, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
    }
  },

  addToCart: async (courseId: number) => {
    set({ isLoading: true });
    try {
      const res = await apiClient.post('/cart/items', { course_id: courseId });
      set({ cart: res.data, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
      throw err;
    }
  },

  removeFromCart: async (courseId: number) => {
    set({ isLoading: true });
    try {
      const res = await apiClient.delete(`/cart/items/${courseId}`);
      set({ cart: res.data, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
    }
  },

  applyCoupon: async (code: string) => {
    const currentSubtotal = get().cart?.subtotal || 0;
    try {
      const res = await apiClient.get('/coupons/validate', { params: { code, subtotal: currentSubtotal } });
      set({ couponCode: code, discountMessage: res.data.message });
      await get().fetchCart(code);
    } catch (err: any) {
      const msg = err.response?.data?.detail || 'Invalid coupon code';
      set({ discountMessage: msg });
      throw new Error(msg);
    }
  },

  clearCart: async () => {
    try {
      await apiClient.delete('/cart/clear');
      set({ cart: null, couponCode: '', discountMessage: null });
    } catch (e) {}
  }
}));
