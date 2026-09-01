import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { HomePage } from '../pages/HomePage';
import { CoursesPage } from '../pages/CoursesPage';
import { CourseDetailPage } from '../pages/CourseDetailPage';
import { CartPage } from '../pages/CartPage';
import { CheckoutPage } from '../pages/CheckoutPage';
import { OrderSuccessPage } from '../pages/OrderSuccessPage';
import { CourseLearningPage } from '../pages/CourseLearningPage';
import { CertificateVerifyPage } from '../pages/CertificateVerifyPage';
import { StudentDashboardPage } from '../pages/StudentDashboardPage';
import { InstructorDashboardPage } from '../pages/InstructorDashboardPage';
import { AdminDashboardPage } from '../pages/AdminDashboardPage';
import { LoginPage } from '../pages/LoginPage';
import { RegisterPage } from '../pages/RegisterPage';
import { ProfilePage } from '../pages/ProfilePage';
import { ProtectedRoute } from './ProtectedRoute';
import { RoleRoute } from './RoleRoute';

export const AppRoutes: React.FC = () => {
  return (
    <Routes>
      {/* Public Discovery Routes */}
      <Route path="/" element={<HomePage />} />
      <Route path="/courses" element={<CoursesPage />} />
      <Route path="/courses/:slug" element={<CourseDetailPage />} />
      <Route path="/certificates/verify/:code" element={<CertificateVerifyPage />} />
      <Route path="/cart" element={<CartPage />} />

      {/* Auth Routes */}
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />

      {/* Protected Student Routes */}
      <Route path="/checkout" element={<ProtectedRoute><CheckoutPage /></ProtectedRoute>} />
      <Route path="/order-success/:orderNumber" element={<ProtectedRoute><OrderSuccessPage /></ProtectedRoute>} />
      <Route path="/student/dashboard" element={<ProtectedRoute><StudentDashboardPage /></ProtectedRoute>} />
      <Route path="/learning/course/:courseId" element={<ProtectedRoute><CourseLearningPage /></ProtectedRoute>} />
      <Route path="/profile" element={<ProtectedRoute><ProfilePage /></ProtectedRoute>} />

      {/* Instructor Studio Routes */}
      <Route path="/instructor/dashboard" element={<RoleRoute allowedRoles={['instructor', 'admin']}><InstructorDashboardPage /></RoleRoute>} />

      {/* Admin Operations Routes */}
      <Route path="/admin/dashboard" element={<RoleRoute allowedRoles={['admin']}><AdminDashboardPage /></RoleRoute>} />

      {/* Fallback */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
};
