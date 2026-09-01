from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.coupon import Coupon, CouponUsage
from app.repositories.base import BaseRepository


class CouponRepository(BaseRepository[Coupon]):
    def __init__(self, db: Session):
        super().__init__(Coupon, db)

    def get_by_code(self, code: str) -> Optional[Coupon]:
        return self.db.query(Coupon).filter(Coupon.code == code.strip().upper(), Coupon.active == True).first()

    def record_usage(self, coupon_id: int, user_id: int, order_id: int) -> CouponUsage:
        coupon = self.get(coupon_id)
        if coupon:
            coupon.used_count += 1
        usage = CouponUsage(
            coupon_id=coupon_id,
            user_id=user_id,
            order_id=order_id,
            used_at=datetime.now(timezone.utc)
        )
        self.db.add(usage)
        self.db.commit()
        return usage
