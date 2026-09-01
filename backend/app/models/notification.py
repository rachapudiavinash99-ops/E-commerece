from sqlalchemy import Column, String, Text, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Notification(Base, BaseModelMixin):
    __tablename__ = "notifications"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    notification_type = Column(String(50), default="system", nullable=False) # system, enrollment, course_approval, certificate_issued, order_confirmation
    link_url = Column(String(500), nullable=True)
    is_read = Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="notifications")
