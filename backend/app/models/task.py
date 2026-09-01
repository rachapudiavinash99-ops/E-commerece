from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, Boolean, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class CodingTask(Base, BaseModelMixin):
    __tablename__ = "coding_tasks"

    lesson_id = Column(ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    instructions = Column(Text, nullable=False)
    task_type = Column(String(50), default="coding", nullable=False) # coding, multiple_choice, sql, output_prediction, debugging, true_false, project
    difficulty = Column(String(50), default="medium", nullable=False) # easy, medium, hard, expert
    language = Column(String(50), default="python", nullable=False) # python, javascript, sql, rust, go, etc.
    starter_code = Column(Text, nullable=True)
    solution_code = Column(Text, nullable=True)
    hints = Column(Text, nullable=True) # JSON list or markdown
    points = Column(Integer, default=10, nullable=False)
    time_limit_seconds = Column(Integer, default=5, nullable=False)

    lesson = relationship("Lesson", back_populates="coding_tasks")
    test_cases = relationship("TestCase", back_populates="task", cascade="all, delete-orphan")
    submissions = relationship("TaskSubmission", back_populates="task", cascade="all, delete-orphan")


class TestCase(Base, BaseModelMixin):
    __tablename__ = "test_cases"

    task_id = Column(ForeignKey("coding_tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    input_data = Column(Text, nullable=True)
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False, nullable=False)
    explanation = Column(Text, nullable=True)

    task = relationship("CodingTask", back_populates="test_cases")


class TaskSubmission(Base, BaseModelMixin):
    __tablename__ = "task_submissions"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    task_id = Column(ForeignKey("coding_tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    submitted_code = Column(Text, nullable=False)
    status = Column(String(50), default="passed", nullable=False) # passed, failed, syntax_error, runtime_error, timeout
    output = Column(Text, nullable=True)
    execution_time_ms = Column(Float, default=0.0, nullable=False)
    score = Column(Integer, default=0, nullable=False)
    submitted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    user = relationship("User", back_populates="task_submissions")
    task = relationship("CodingTask", back_populates="submissions")
