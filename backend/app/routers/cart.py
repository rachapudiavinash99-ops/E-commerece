from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, http_409_conflict, ResourceConflictError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.cart import AddToCartRequest, CartResponse
from app.services.cart_service import CartService

router = APIRouter(prefix="/cart", tags=["Shopping Cart"])


@router.get("", response_model=CartResponse)
def get_cart(
    coupon_code: Optional[str] = None,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CartService(db)
    return service.get_cart_summary(user.id, coupon_code=coupon_code)


@router.post("/items", response_model=CartResponse)
def add_item(
    req: AddToCartRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CartService(db)
    try:
        return service.add_to_cart(user.id, req.course_id)
    except ResourceConflictError as e:
        raise http_409_conflict(str(e.message))


@router.delete("/items/{course_id}", response_model=CartResponse)
def remove_item(
    course_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CartService(db)
    return service.remove_from_cart(user.id, course_id)


@router.delete("/clear", response_model=CartResponse)
def clear_cart(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CartService(db)
    service.clear_cart(user.id)
    return service.get_cart_summary(user.id)
