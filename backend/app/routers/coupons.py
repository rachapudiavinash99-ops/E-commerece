from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, CouponValidationError
from app.schemas.coupon import ApplyCouponResponse
from app.services.coupon_service import CouponService

router = APIRouter(prefix="/coupons", tags=["Coupons"])


@router.get("/validate", response_model=ApplyCouponResponse)
def validate_coupon(
    code: str = Query(...),
    subtotal: float = Query(...),
    db: Session = Depends(get_db)
):
    service = CouponService(db)
    try:
        return service.validate_coupon(code, subtotal)
    except CouponValidationError as e:
        raise http_400_bad_request(str(e.message))
