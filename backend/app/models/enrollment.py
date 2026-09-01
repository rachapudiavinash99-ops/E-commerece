from datetime import datetime
from sqlalchemy import Column, Float, Boolean, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Enrollment(Base, BaseModelMixin):
    __tablename__ = "enrollments"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id = Column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(ForeignKey("orders.id", ondelete="SET NULL"), nullable=True)
    enrolled_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completion_percentage = Column(Float, default=0.0, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    last_accessed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    order = relationship("Order", back_populates="enrollments")
