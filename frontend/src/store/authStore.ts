import { create } from 'zustand';
import { User, UserRole } from '../types';
import { apiClient } from '../api/client';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, pass: string) => Promise<void>;
  register: (payload: { email: string; password: string; full_name: string; role?: string }) => Promise<void>;
  logout: () => void;
  loadUser: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: JSON.parse(localStorage.getItem('user_info') || 'null'),
  token: localStorage.getItem('access_token'),
  isAuthenticated: !!localStorage.getItem('access_token'),
  isLoading: false,

  login: async (email, password) => {
    set({ isLoading: true });
    try {
      const res = await apiClient.post('/auth/login', { email, password });
      const { access_token, refresh_token, user_id, full_name, role, avatar_url } = res.data;
      const userObj: User = {
        id: user_id,
        email,
        full_name,
        role: role as UserRole,
        avatar_url,
        is_active: true,
        is_verified: true,
        created_at: new Date().toISOString()
      };
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);
      localStorage.setItem('user_info', JSON.stringify(userObj));
      set({ user: userObj, token: access_token, isAuthenticated: true, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
      throw err;
    }
  },

  register: async (payload) => {
    set({ isLoading: true });
    try {
      const res = await apiClient.post('/auth/register', payload);
      const { access_token, refresh_token, user_id, email, full_name, role, avatar_url } = res.data;
      const userObj: User = {
        id: user_id,
        email,
        full_name,
        role: role as UserRole,
        avatar_url,
        is_active: true,
        is_verified: true,
        created_at: new Date().toISOString()
      };
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);
      localStorage.setItem('user_info', JSON.stringify(userObj));
      set({ user: userObj, token: access_token, isAuthenticated: true, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
      throw err;
    }
  },

  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_info');
    set({ user: null, token: null, isAuthenticated: false });
  },

  loadUser: async () => {
    const token = localStorage.getItem('access_token');
    if (!token) return;
    try {
      const res = await apiClient.get('/auth/me');
      set({ user: res.data, isAuthenticated: true });
      localStorage.setItem('user_info', JSON.stringify(res.data));
    } catch (e) {
      set({ user: null, token: null, isAuthenticated: false });
    }
  }
}));
