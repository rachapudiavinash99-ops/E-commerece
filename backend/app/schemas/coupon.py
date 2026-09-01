from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field


class CouponBase(BaseModel):
    code: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = None
    discount_type: str = Field("percentage", pattern="^(percentage|fixed_amount)$")
    discount_value: float = Field(..., gt=0.0)
    minimum_amount: float = 0.0
    maximum_discount: Optional[float] = None
    expiry_date: Optional[datetime] = None
    usage_limit: int = 100
    active: bool = True


class CouponCreate(CouponBase):
    pass


class CouponUpdate(BaseModel):
    description: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    minimum_amount: Optional[float] = None
    maximum_discount: Optional[float] = None
    expiry_date: Optional[datetime] = None
    usage_limit: Optional[int] = None
    active: Optional[bool] = None


class CouponResponse(CouponBase):
    id: int
    used_count: int

    model_config = ConfigDict(from_attributes=True)


class ApplyCouponRequest(BaseModel):
    code: str


class ApplyCouponResponse(BaseModel):
    valid: bool
    code: str
    discount_amount: float
    new_total: float
    message: str
