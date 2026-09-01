from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel


class PaymentInitiateRequest(BaseModel):
    order_id: int
    payment_method: str = "mock_gateway"


class PaymentInitiateResponse(BaseModel):
    transaction_id: str
    order_id: int
    amount: float
    currency: str
    status: str
    payment_url: Optional[str] = None
    client_secret: Optional[str] = None


class PaymentVerifyRequest(BaseModel):
    transaction_id: str
    order_id: int
    simulate_failure: bool = False


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    transaction_id: str
    amount: float
    currency: str
    status: str
    payment_method: str
    paid_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
