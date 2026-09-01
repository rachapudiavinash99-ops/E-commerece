from datetime import datetime
from sqlalchemy import Column, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Payment(Base, BaseModelMixin):
    __tablename__ = "payments"

    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    transaction_id = Column(String(100), unique=True, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    status = Column(String(50), default="initiated", nullable=False) # initiated, successful, failed, refunded
    payment_method = Column(String(50), default="mock_gateway", nullable=False)
    payload = Column(Text, nullable=True) # JSON store of payment gateway response
    paid_at = Column(DateTime, nullable=True)

    order = relationship("Order", back_populates="payment")
    transactions = relationship("PaymentTransaction", back_populates="payment", cascade="all, delete-orphan")


class PaymentTransaction(Base, BaseModelMixin):
    __tablename__ = "payment_transactions"

    payment_id = Column(ForeignKey("payments.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = Column(String(100), nullable=False) # payment.created, payment.authorized, payment.captured, payment.failed
    status = Column(String(50), nullable=False)
    response_data = Column(Text, nullable=True)

    payment = relationship("Payment", back_populates="transactions")
