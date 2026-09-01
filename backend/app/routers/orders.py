from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, ValidationError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.order import CheckoutRequest, OrderResponse
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/checkout", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def checkout_cart(
    req: CheckoutRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    try:
        return service.create_order_from_cart(user.id, coupon_code=req.coupon_code)
    except ValidationError as e:
        raise http_400_bad_request(str(e.message))


@router.get("", response_model=List[OrderResponse])
def get_user_orders(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    return service.order_repo.get_user_orders(user.id)


@router.get("/{order_number}", response_model=OrderResponse)
def get_order_by_number(
    order_number: str,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    return service.get_order_by_number(order_number)
