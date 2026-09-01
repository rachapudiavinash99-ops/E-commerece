from datetime import datetime
from sqlalchemy import Column, String, Text, Float, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import BaseModelMixin


class Certificate(Base, BaseModelMixin):
    __tablename__ = "certificates"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id = Column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    certificate_number = Column(String(100), unique=True, nullable=False, index=True)
    verification_code = Column(String(120), unique=True, nullable=False, index=True)
    verification_hash = Column(String(255), nullable=False)
    final_grade = Column(Float, default=100.0, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    pdf_url = Column(String(500), nullable=True)
    svg_content = Column(Text, nullable=True)

    user = relationship("User", back_populates="certificates")
    course = relationship("Course", back_populates="certificates")
