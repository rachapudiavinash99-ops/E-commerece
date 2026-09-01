import { describe, it, expect } from 'vitest';
import { useCartStore } from '../store/cartStore';

describe('Cart Store', () => {
  it('initializes with empty cart and zero items', () => {
    const state = useCartStore.getState();
    expect(state.cart).toBeNull();
    expect(state.isLoading).toBe(false);
  });
});
