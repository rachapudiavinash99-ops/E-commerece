from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field
from app.schemas.user import UserPublicResponse


class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    title: Optional[str] = Field(None, max_length=200)
    comment: str = Field(..., min_length=5)


class ReviewCreate(ReviewBase):
    course_id: int


class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(None, ge=1, le=5)
    title: Optional[str] = None
    comment: Optional[str] = None


class ReviewResponse(ReviewBase):
    id: int
    course_id: int
    user_id: int
    is_verified_purchase: bool
    status: str
    helpful_count: int
    created_at: datetime
    user: Optional[UserPublicResponse] = None

    model_config = ConfigDict(from_attributes=True)
