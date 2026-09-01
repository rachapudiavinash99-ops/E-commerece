from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class LessonProgress(Base, BaseModelMixin):
    __tablename__ = "lesson_progresses"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    lesson_id = Column(ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False, index=True)
    completed = Column(Boolean, default=False, nullable=False)
    watched_seconds = Column(Integer, default=0, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    last_accessed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="lesson_progresses")
    lesson = relationship("Lesson", back_populates="progresses")
