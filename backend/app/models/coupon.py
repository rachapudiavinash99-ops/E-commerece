from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Coupon(Base, BaseModelMixin):
    __tablename__ = "coupons"

    code = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)
    discount_type = Column(String(50), default="percentage", nullable=False) # percentage, fixed_amount
    discount_value = Column(Float, nullable=False)
    minimum_amount = Column(Float, default=0.0, nullable=False)
    maximum_discount = Column(Float, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    usage_limit = Column(Integer, default=100, nullable=False)
    used_count = Column(Integer, default=0, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    orders = relationship("Order", back_populates="coupon")
    usages = relationship("CouponUsage", back_populates="coupon", cascade="all, delete-orphan")


class CouponUsage(Base, BaseModelMixin):
    __tablename__ = "coupon_usages"

    coupon_id = Column(ForeignKey("coupons.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    used_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    coupon = relationship("Coupon", back_populates="usages")
    order = relationship("Order")
