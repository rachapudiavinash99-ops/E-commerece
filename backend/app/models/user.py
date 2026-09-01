from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class User(Base, BaseModelMixin):
    __tablename__ = "users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    role = Column(String(50), default="student", nullable=False, index=True) # student, instructor, admin
    headline = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(500), nullable=True)
    website_url = Column(String(255), nullable=True)
    github_url = Column(String(255), nullable=True)
    twitter_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    verification_token = Column(String(255), nullable=True)
    reset_password_token = Column(String(255), nullable=True)
    reset_token_expires_at = Column(DateTime, nullable=True)
    last_login_at = Column(DateTime, nullable=True)

    # Relationships
    authored_courses = relationship("Course", back_populates="instructor", cascade="all, delete-orphan")
    enrollments = relationship("Enrollment", back_populates="user", cascade="all, delete-orphan")
    lesson_progresses = relationship("LessonProgress", back_populates="user", cascade="all, delete-orphan")
    task_submissions = relationship("TaskSubmission", back_populates="user", cascade="all, delete-orphan")
    quiz_attempts = relationship("QuizAttempt", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    certificates = relationship("Certificate", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")
    cart = relationship("Cart", back_populates="user", uselist=False, cascade="all, delete-orphan")
    activity_logs = relationship("UserActivityLog", back_populates="user", cascade="all, delete-orphan")


class RefreshToken(Base, BaseModelMixin):
    __tablename__ = "refresh_tokens"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    token = Column(String(500), unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_revoked = Column(Boolean, default=False, nullable=False)
    device_info = Column(String(255), nullable=True)

    user = relationship("User", back_populates="refresh_tokens")


class UserActivityLog(Base, BaseModelMixin):
    __tablename__ = "user_activity_logs"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    action = Column(String(100), nullable=False) # e.g. login, enroll_course, complete_lesson
    details = Column(Text, nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(255), nullable=True)

    user = relationship("User", back_populates="activity_logs")
