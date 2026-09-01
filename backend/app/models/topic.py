from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Topic(Base, BaseModelMixin):
    __tablename__ = "topics"

    category_id = Column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(100), nullable=False, index=True)
    slug = Column(String(120), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(100), default="code", nullable=False)
    display_order = Column(Integer, default=0, nullable=False)
    is_popular = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    category = relationship("Category", back_populates="topics")
    courses = relationship("Course", back_populates="topic", cascade="all, delete-orphan")
