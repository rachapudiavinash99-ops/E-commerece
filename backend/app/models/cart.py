from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Cart(Base, BaseModelMixin):
    __tablename__ = "carts"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=True, index=True)
    session_id = Column(String(255), unique=True, nullable=True, index=True)

    user = relationship("User", back_populates="cart")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(Base, BaseModelMixin):
    __tablename__ = "cart_items"

    cart_id = Column(ForeignKey("carts.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id = Column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    added_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    cart = relationship("Cart", back_populates="items")
    course = relationship("Course", back_populates="cart_items")
