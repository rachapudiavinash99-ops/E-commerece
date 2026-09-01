from sqlalchemy import Column, String, Float, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Order(Base, BaseModelMixin):
    __tablename__ = "orders"

    order_number = Column(String(100), unique=True, nullable=False, index=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    subtotal = Column(Float, default=0.0, nullable=False)
    discount = Column(Float, default=0.0, nullable=False)
    tax = Column(Float, default=0.0, nullable=False)
    total = Column(Float, default=0.0, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    payment_status = Column(String(50), default="initiated", nullable=False) # initiated, successful, failed, refunded
    order_status = Column(String(50), default="pending", nullable=False) # pending, completed, failed, cancelled, refunded
    coupon_id = Column(ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="orders")
    coupon = relationship("Coupon", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    payment = relationship("Payment", back_populates="order", uselist=False, cascade="all, delete-orphan")
    enrollments = relationship("Enrollment", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base, BaseModelMixin):
    __tablename__ = "order_items"

    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id = Column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")
    course = relationship("Course", back_populates="order_items")
