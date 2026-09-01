export type UserRole = 'student' | 'instructor' | 'admin';

export interface User {
  id: number;
  email: string;
  full_name: string;
  role: UserRole;
  headline?: string;
  bio?: string;
  avatar_url?: string;
  website_url?: string;
  github_url?: string;
  twitter_url?: string;
  linkedin_url?: string;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
  user: User;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  description?: string;
  icon: string;
  image_url?: string;
  display_order: number;
  course_count?: number;
  topics?: Topic[];
}

export interface Topic {
  id: number;
  category_id: number;
  name: string;
  slug: string;
  description?: string;
  icon: string;
  is_popular: boolean;
  course_count?: number;
  category?: Category;
}

export interface Course {
  id: number;
  instructor_id: number;
  topic_id: number;
  title: string;
  slug: string;
  subtitle?: string;
  description: string;
  short_description?: string;
  price: number;
  discount_price?: number;
  level: 'beginner' | 'intermediate' | 'advanced' | 'all_levels';
  language: string;
  duration_hours: number;
  thumbnail_url?: string;
  promo_video_url?: string;
  requirements?: string;
  what_you_will_learn?: string;
  target_audience?: string;
  status: 'draft' | 'pending_approval' | 'published' | 'rejected' | 'archived';
  is_featured: boolean;
  is_bestseller: boolean;
  average_rating: number;
  review_count: number;
  student_count: number;
  instructor?: User;
  topic?: Topic;
  modules?: Module[];
  created_at: string;
  published_at?: string;
}

export interface Module {
  id: number;
  course_id: number;
  title: string;
  description?: string;
  order_index: number;
  is_published: boolean;
  lessons: Lesson[];
}

export interface Lesson {
  id: number;
  module_id: number;
  title: string;
  slug: string;
  lesson_type: 'video' | 'article' | 'coding_task' | 'quiz';
  content?: string;
  video_url?: string;
  duration_minutes: number;
  order_index: number;
  is_preview: boolean;
  is_published: boolean;
  coding_tasks?: CodingTask[];
  quizzes?: Quiz[];
}

export interface CodingTask {
  id: number;
  lesson_id: number;
  title: string;
  instructions: string;
  task_type: string;
  difficulty: string;
  language: string;
  starter_code?: string;
  solution_code?: string;
  hints?: string;
  points: number;
  time_limit_seconds: number;
  test_cases: TestCase[];
}

export interface TestCase {
  id: number;
  input_data?: string;
  expected_output: string;
  is_hidden: boolean;
  explanation?: string;
}

export interface TaskSubmissionResult {
  id: number;
  task_id: number;
  status: 'passed' | 'failed' | 'syntax_error' | 'runtime_error' | 'timeout';
  output?: string;
  execution_time_ms: number;
  score: number;
  total_points: number;
  passed_test_cases: number;
  total_test_cases: number;
  details?: string;
  submitted_at: string;
}

export interface Quiz {
  id: number;
  lesson_id: number;
  title: string;
  description?: string;
  pass_percentage: number;
  time_limit_minutes: number;
  max_attempts: number;
  questions: QuizQuestion[];
}

export interface QuizQuestion {
  id: number;
  quiz_id: number;
  question_text: string;
  question_type: string;
  code_snippet?: string;
  explanation?: string;
  points: number;
  order_index: number;
  options: QuizOption[];
}

export interface QuizOption {
  id: number;
  question_id: number;
  option_text: string;
  order_index: number;
}

export interface QuizAttemptResult {
  id: number;
  quiz_id: number;
  score: number;
  total_points: number;
  passed: boolean;
  correct_count: number;
  total_questions: number;
  completed_at: string;
  answers_breakdown?: Record<string, any>;
}

export interface CartItem {
  id: number;
  course_id: number;
  added_at: string;
  course: Course;
}

export interface Cart {
  id: number;
  user_id?: number;
  items: CartItem[];
  item_count: number;
  subtotal: number;
  discount: number;
  tax: number;
  total: number;
  applied_coupon?: string;
}

export interface Order {
  id: number;
  order_number: string;
  user_id: number;
  subtotal: number;
  discount: number;
  tax: number;
  total: number;
  currency: string;
  payment_status: string;
  order_status: string;
  created_at: string;
  items: { id: number; course_id: number; price: number; course: Course }[];
}

export interface Enrollment {
  id: number;
  user_id: number;
  course_id: number;
  enrolled_at: string;
  completion_percentage: number;
  is_completed: boolean;
  completed_at?: string;
  last_accessed_at: string;
  course: Course;
}

export interface CourseProgressState {
  course_id: number;
  completion_percentage: number;
  is_completed: boolean;
  completed_lessons_count: number;
  total_lessons_count: number;
  completed_lesson_ids: number[];
  certificate_id?: number;
}

export interface Certificate {
  id: number;
  certificate_number: string;
  verification_code: string;
  verification_hash: string;
  final_grade: number;
  issued_at: string;
  svg_content?: string;
  course?: Course;
  user?: User;
}

export interface CertificateVerifyResult {
  is_valid: boolean;
  certificate_number: string;
  verification_code: string;
  student_name: string;
  course_title: string;
  instructor_name: string;
  issued_at: string;
  grade: number;
  message: string;
}

export interface Review {
  id: number;
  course_id: number;
  user_id: number;
  rating: number;
  title?: string;
  comment: string;
  is_verified_purchase: boolean;
  helpful_count: number;
  created_at: string;
  user?: User;
}

export interface Notification {
  id: number;
  title: string;
  message: string;
  notification_type: string;
  link_url?: string;
  is_read: boolean;
  created_at: string;
}

export interface PaginatedResult<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  has_next: boolean;
  has_prev: boolean;
}
