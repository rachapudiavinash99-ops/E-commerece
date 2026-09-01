from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Lesson(Base, BaseModelMixin):
    __tablename__ = "lessons"

    module_id = Column(ForeignKey("modules.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(220), nullable=False)
    lesson_type = Column(String(50), default="video", nullable=False) # video, article, coding_task, quiz
    content = Column(Text, nullable=True) # Rich markdown or html text
    video_url = Column(String(500), nullable=True)
    duration_minutes = Column(Integer, default=10, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)
    is_preview = Column(Boolean, default=False, nullable=False)
    is_published = Column(Boolean, default=True, nullable=False)

    module = relationship("Module", back_populates="lessons")
    resources = relationship("LessonResource", back_populates="lesson", cascade="all, delete-orphan")
    coding_tasks = relationship("CodingTask", back_populates="lesson", cascade="all, delete-orphan")
    quizzes = relationship("Quiz", back_populates="lesson", cascade="all, delete-orphan")
    progresses = relationship("LessonProgress", back_populates="lesson", cascade="all, delete-orphan")


class LessonResource(Base, BaseModelMixin):
    __tablename__ = "lesson_resources"

    lesson_id = Column(ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    file_url = Column(String(500), nullable=False)
    resource_type = Column(String(50), default="pdf", nullable=False) # pdf, zip, code, link
    size_bytes = Column(Integer, default=0, nullable=False)

    lesson = relationship("Lesson", back_populates="resources")
