"""Base model class with common auditing fields: ID, timestamps, and dictionary serialization."""
from datetime import datetime, timezone
from typing import Any, Dict
from sqlalchemy import Column, Integer, DateTime
from app.core.database import Base


class TimestampMixin:
    """Audit timestamps mixin for SQLAlchemy models."""
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )


class BaseModelMixin(TimestampMixin):
    """Primary base model mixin with integer identity key and serialization helper."""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    def to_dict(self) -> Dict[str, Any]:
        """Convert model instance attributes to a plain Python dictionary."""
        result: Dict[str, Any] = {}
        for col in self.__table__.columns:
            val = getattr(self, col.name)
            if isinstance(val, datetime):
                result[col.name] = val.isoformat()
            else:
                result[col.name] = val
        return result

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
