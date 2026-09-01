from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Category(Base, BaseModelMixin):
    __tablename__ = "categories"

    name = Column(String(100), unique=True, nullable=False, index=True)
    slug = Column(String(120), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(100), default="folder", nullable=False)
    image_url = Column(String(500), nullable=True)
    display_order = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    topics = relationship("Topic", back_populates="category", cascade="all, delete-orphan", order_by="Topic.display_order")
