from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Float, Integer, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Course(Base, BaseModelMixin):
    __tablename__ = "courses"

    instructor_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    topic_id = Column(ForeignKey("topics.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(280), unique=True, nullable=False, index=True)
    subtitle = Column(String(300), nullable=True)
    description = Column(Text, nullable=False)
    short_description = Column(String(500), nullable=True)
    price = Column(Float, default=0.0, nullable=False)
    discount_price = Column(Float, nullable=True)
    level = Column(String(50), default="all_levels", nullable=False) # beginner, intermediate, advanced, all_levels
    language = Column(String(50), default="English", nullable=False)
    duration_hours = Column(Float, default=0.0, nullable=False)
    thumbnail_url = Column(String(500), nullable=True)
    promo_video_url = Column(String(500), nullable=True)
    requirements = Column(Text, nullable=True) # JSON or newline separated
    what_you_will_learn = Column(Text, nullable=True) # JSON or newline separated
    target_audience = Column(Text, nullable=True)
    status = Column(String(50), default="draft", nullable=False, index=True) # draft, pending_approval, published, rejected, archived
    is_featured = Column(Boolean, default=False, nullable=False)
    is_bestseller = Column(Boolean, default=False, nullable=False)
    average_rating = Column(Float, default=0.0, nullable=False)
    review_count = Column(Integer, default=0, nullable=False)
    student_count = Column(Integer, default=0, nullable=False)
    published_at = Column(DateTime, nullable=True)

    # Relationships
    instructor = relationship("User", back_populates="authored_courses")
    topic = relationship("Topic", back_populates="courses")
    modules = relationship("Module", back_populates="course", cascade="all, delete-orphan", order_by="Module.order_index")
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="course", cascade="all, delete-orphan")
    certificates = relationship("Certificate", back_populates="course", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="course", cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="course", cascade="all, delete-orphan")
