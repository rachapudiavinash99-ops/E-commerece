from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Quiz(Base, BaseModelMixin):
    __tablename__ = "quizzes"

    lesson_id = Column(ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    pass_percentage = Column(Integer, default=70, nullable=False)
    time_limit_minutes = Column(Integer, default=15, nullable=False)
    max_attempts = Column(Integer, default=3, nullable=False)

    lesson = relationship("Lesson", back_populates="quizzes")
    questions = relationship("QuizQuestion", back_populates="quiz", cascade="all, delete-orphan", order_by="QuizQuestion.order_index")
    attempts = relationship("QuizAttempt", back_populates="quiz", cascade="all, delete-orphan")


class QuizQuestion(Base, BaseModelMixin):
    __tablename__ = "quiz_questions"

    quiz_id = Column(ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False, index=True)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(50), default="single_choice", nullable=False) # single_choice, multiple_choice, true_false, output_prediction
    code_snippet = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    points = Column(Integer, default=1, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)

    quiz = relationship("Quiz", back_populates="questions")
    options = relationship("QuizOption", back_populates="question", cascade="all, delete-orphan", order_by="QuizOption.order_index")


class QuizOption(Base, BaseModelMixin):
    __tablename__ = "quiz_options"

    question_id = Column(ForeignKey("quiz_questions.id", ondelete="CASCADE"), nullable=False, index=True)
    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)

    question = relationship("QuizQuestion", back_populates="options")


class QuizAttempt(Base, BaseModelMixin):
    __tablename__ = "quiz_attempts"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    quiz_id = Column(ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False, index=True)
    score = Column(Float, default=0.0, nullable=False)
    total_points = Column(Integer, default=0, nullable=False)
    passed = Column(Boolean, default=False, nullable=False)
    answers_json = Column(Text, nullable=True) # JSON store of user's selected options
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="quiz_attempts")
    quiz = relationship("Quiz", back_populates="attempts")
