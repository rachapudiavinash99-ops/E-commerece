from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field
from app.schemas.category import CategoryResponse


class TopicBase(BaseModel):
    category_id: int
    name: str = Field(..., min_length=2, max_length=100)
    slug: str = Field(..., min_length=2, max_length=120)
    description: Optional[str] = None
    icon: str = Field("code", max_length=100)
    display_order: int = 0
    is_popular: bool = False
    is_active: bool = True


class TopicCreate(TopicBase):
    pass


class TopicUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    display_order: Optional[int] = None
    is_popular: Optional[bool] = None
    is_active: Optional[bool] = None


class TopicResponse(TopicBase):
    id: int
    course_count: Optional[int] = 0
    category: Optional[CategoryResponse] = None

    model_config = ConfigDict(from_attributes=True)
