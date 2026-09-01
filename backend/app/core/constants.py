"""System-wide enumerations and constant values for the CodePulse Academy platform."""
from enum import Enum


class UserRole(str, Enum):
    """User authorization roles."""
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"


class CourseStatus(str, Enum):
    """Course lifecycle states."""
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    PUBLISHED = "published"
    REJECTED = "rejected"
    ARCHIVED = "archived"


class CourseLevel(str, Enum):
    """Difficulty levels for courses."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    ALL_LEVELS = "all_levels"


class LessonType(str, Enum):
    """Types of educational lesson units."""
    VIDEO = "video"
    ARTICLE = "article"
    CODING_TASK = "coding_task"
    QUIZ = "quiz"


class TaskType(str, Enum):
    """Interactive programming task modalities."""
    CODING = "coding"
    MULTIPLE_CHOICE = "multiple_choice"
    SQL = "sql"
    OUTPUT_PREDICTION = "output_prediction"
    DEBUGGING = "debugging"
    TRUE_FALSE = "true_false"
    PROJECT = "project"


class TaskDifficulty(str, Enum):
    """Task complexity classification."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


class SubmissionStatus(str, Enum):
    """Execution status for student code submissions."""
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"
    SYNTAX_ERROR = "syntax_error"
    RUNTIME_ERROR = "runtime_error"
    TIMEOUT = "timeout"


class QuestionType(str, Enum):
    """Quiz question format types."""
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    OUTPUT_PREDICTION = "output_prediction"


class DiscountType(str, Enum):
    """Coupon discount calculation methods."""
    PERCENTAGE = "percentage"
    FIXED_AMOUNT = "fixed_amount"


class OrderStatus(str, Enum):
    """Lifecycle states of shopping cart orders."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class PaymentStatus(str, Enum):
    """Payment transaction states."""
    INITIATED = "initiated"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"


class PaymentMethod(str, Enum):
    """Supported payment methods."""
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    STRIPE = "stripe"
    RAZORPAY = "razorpay"
    MOCK_GATEWAY = "mock_gateway"


class ReviewStatus(str, Enum):
    """Moderation status of student course reviews."""
    APPROVED = "approved"
    PENDING = "pending"
    FLAGGED = "flagged"
    REJECTED = "rejected"


class NotificationType(str, Enum):
    """Classification of notification events."""
    SYSTEM = "system"
    ENROLLMENT = "enrollment"
    COURSE_UPDATE = "course_update"
    COURSE_APPROVAL = "course_approval"
    COURSE_REJECTION = "course_rejection"
    ORDER_CONFIRMATION = "order_confirmation"
    CERTIFICATE_ISSUED = "certificate_issued"
    REVIEW_RECEIVED = "review_received"
    TASK_FEEDBACK = "task_feedback"
