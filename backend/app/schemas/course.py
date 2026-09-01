from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field
from app.schemas.user import UserPublicResponse
from app.schemas.topic import TopicResponse


class CourseBase(BaseModel):
    topic_id: int
    title: str = Field(..., min_length=5, max_length=255)
    slug: str = Field(..., min_length=5, max_length=280)
    subtitle: Optional[str] = None
    description: str = Field(..., min_length=20)
    short_description: Optional[str] = None
    price: float = Field(0.0, ge=0.0)
    discount_price: Optional[float] = Field(None, ge=0.0)
    level: str = Field("all_levels", pattern="^(beginner|intermediate|advanced|all_levels)$")
    language: str = "English"
    duration_hours: float = 0.0
    thumbnail_url: Optional[str] = None
    promo_video_url: Optional[str] = None
    requirements: Optional[str] = None
    what_you_will_learn: Optional[str] = None
    target_audience: Optional[str] = None


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    topic_id: Optional[int] = None
    title: Optional[str] = None
    slug: Optional[str] = None
    subtitle: Optional[str] = None
    description: Optional[str] = None
    short_description: Optional[str] = None
    price: Optional[float] = None
    discount_price: Optional[float] = None
    level: Optional[str] = None
    language: Optional[str] = None
    duration_hours: Optional[float] = None
    thumbnail_url: Optional[str] = None
    promo_video_url: Optional[str] = None
    requirements: Optional[str] = None
    what_you_will_learn: Optional[str] = None
    target_audience: Optional[str] = None
    status: Optional[str] = None


class CourseStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(draft|pending_approval|published|rejected|archived)$")
    feedback: Optional[str] = None


class CourseCardResponse(BaseModel):
    id: int
    title: str
    slug: str
    subtitle: Optional[str] = None
    price: float
    discount_price: Optional[float] = None
    level: str
    duration_hours: float
    thumbnail_url: Optional[str] = None
    average_rating: float
    review_count: int
    student_count: int
    is_featured: bool
    is_bestseller: bool
    status: str
    instructor: Optional[UserPublicResponse] = None
    topic: Optional[TopicResponse] = None

    model_config = ConfigDict(from_attributes=True)


class CourseDetailResponse(CourseCardResponse):
    description: str
    short_description: Optional[str] = None
    language: str
    promo_video_url: Optional[str] = None
    requirements: Optional[str] = None
    what_you_will_learn: Optional[str] = None
    target_audience: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class CourseFilterParams(BaseModel):
    query: Optional[str] = None
    category_id: Optional[int] = None
    topic_id: Optional[int] = None
    level: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    min_rating: Optional[float] = None
    sort_by: Optional[str] = "popularity" # popularity, rating, price_low, price_high, newest
    page: int = 1
    page_size: int = 12
