from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.course import CourseCardResponse


class CartItemResponse(BaseModel):
    id: int
    course_id: int
    added_at: datetime
    course: CourseCardResponse

    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    items: List[CartItemResponse] = []
    subtotal: float = 0.0
    discount: float = 0.0
    tax: float = 0.0
    total: float = 0.0
    applied_coupon: Optional[str] = None
    item_count: int = 0


class AddToCartRequest(BaseModel):
    course_id: int
