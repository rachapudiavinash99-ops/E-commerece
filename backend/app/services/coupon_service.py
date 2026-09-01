from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from app.core.exceptions import CouponValidationError, ResourceNotFoundError
from app.models.coupon import Coupon
from app.repositories.coupon_repository import CouponRepository


class CouponService:
    def __init__(self, db: Session):
        self.db = db
        self.coupon_repo = CouponRepository(db)

    def validate_coupon(self, code: str, current_subtotal: float) -> dict:
        coupon = self.coupon_repo.get_by_code(code)
        if not coupon:
            raise CouponValidationError(f"Coupon code '{code}' is invalid or inactive.")

        if coupon.usage_limit and coupon.used_count >= coupon.usage_limit:
            raise CouponValidationError(f"Coupon code '{code}' has exceeded its maximum usage limit.")

        if coupon.expiry_date and coupon.expiry_date < datetime.now(timezone.utc):
            raise CouponValidationError(f"Coupon code '{code}' has expired.")

        if current_subtotal < coupon.minimum_amount:
            raise CouponValidationError(f"Minimum order spend of ${coupon.minimum_amount:.2f} is required for this coupon.")

        if coupon.discount_type == "percentage":
            discount = current_subtotal * (coupon.discount_value / 100.0)
            if coupon.maximum_discount:
                discount = min(discount, coupon.maximum_discount)
        else:
            discount = min(coupon.discount_value, current_subtotal)

        new_total = max(0.0, current_subtotal - discount)
        return {
            "valid": True,
            "code": coupon.code,
            "discount_amount": round(discount, 2),
            "new_total": round(new_total, 2),
            "message": f"Coupon applied: ${discount:.2f} discount savings!"
        }
