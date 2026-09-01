from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Review(Base, BaseModelMixin):
    __tablename__ = "reviews"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id = Column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    rating = Column(Integer, nullable=False) # 1 to 5
    title = Column(String(200), nullable=True)
    comment = Column(Text, nullable=False)
    is_verified_purchase = Column(Boolean, default=True, nullable=False)
    status = Column(String(50), default="approved", nullable=False) # approved, pending, flagged, rejected
    helpful_count = Column(Integer, default=0, nullable=False)

    user = relationship("User", back_populates="reviews")
    course = relationship("Course", back_populates="reviews")
    helpful_votes = relationship("ReviewHelpful", back_populates="review", cascade="all, delete-orphan")


class ReviewHelpful(Base, BaseModelMixin):
    __tablename__ = "review_helpful_votes"

    review_id = Column(ForeignKey("reviews.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    is_helpful = Column(Boolean, default=True, nullable=False)

    review = relationship("Review", back_populates="helpful_votes")
