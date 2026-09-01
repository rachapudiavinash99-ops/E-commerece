from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.course import CourseCardResponse


class OrderItemResponse(BaseModel):
    id: int
    course_id: int
    price: float
    course: CourseCardResponse

    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    id: int
    order_number: str
    user_id: int
    subtotal: float
    discount: float
    tax: float
    total: float
    currency: str
    payment_status: str
    order_status: str
    created_at: datetime
    items: List[OrderItemResponse] = []

    model_config = ConfigDict(from_attributes=True)


class CheckoutRequest(BaseModel):
    coupon_code: Optional[str] = None
    payment_method: str = "mock_gateway"
    billing_address: Optional[dict] = None
