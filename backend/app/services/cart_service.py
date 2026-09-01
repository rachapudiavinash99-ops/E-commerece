from typing import Optional
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, ResourceConflictError
from app.models.cart import Cart
from app.repositories.cart_repository import CartRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.coupon_repository import CouponRepository


class CartService:
    def __init__(self, db: Session):
        self.db = db
        self.cart_repo = CartRepository(db)
        self.course_repo = CourseRepository(db)
        self.enrollment_repo = EnrollmentRepository(db)
        self.coupon_repo = CouponRepository(db)

    def get_cart_summary(self, user_id: int, coupon_code: Optional[str] = None) -> dict:
        cart = self.cart_repo.get_or_create_user_cart(user_id)
        items = cart.items

        subtotal = 0.0
        for item in items:
            price = item.course.discount_price if item.course.discount_price is not None else item.course.price
            subtotal += price

        discount = 0.0
        if coupon_code:
            coupon = self.coupon_repo.get_by_code(coupon_code)
            if coupon and subtotal >= coupon.minimum_amount:
                if coupon.discount_type == "percentage":
                    discount = subtotal * (coupon.discount_value / 100.0)
                    if coupon.maximum_discount:
                        discount = min(discount, coupon.maximum_discount)
                else:
                    discount = min(coupon.discount_value, subtotal)

        tax = round((subtotal - discount) * 0.05, 2) if subtotal > 0 else 0.0 # 5% flat estimated tax
        total = max(0.0, round(subtotal - discount + tax, 2))

        return {
            "id": cart.id,
            "user_id": user_id,
            "items": items,
            "item_count": len(items),
            "subtotal": round(subtotal, 2),
            "discount": round(discount, 2),
            "tax": tax,
            "total": total,
            "applied_coupon": coupon_code
        }

    def add_to_cart(self, user_id: int, course_id: int) -> dict:
        # Check if already enrolled
        enrollment = self.enrollment_repo.get_enrollment(user_id, course_id)
        if enrollment:
            raise ResourceConflictError("You are already enrolled in this course.")

        course = self.course_repo.get(course_id)
        if not course:
            raise ResourceNotFoundError("Course", course_id)

        cart = self.cart_repo.get_or_create_user_cart(user_id)
        self.cart_repo.add_course_to_cart(cart.id, course_id)
        return self.get_cart_summary(user_id)

    def remove_from_cart(self, user_id: int, course_id: int) -> dict:
        cart = self.cart_repo.get_or_create_user_cart(user_id)
        self.cart_repo.remove_item(cart.id, course_id)
        return self.get_cart_summary(user_id)

    def clear_cart(self, user_id: int) -> None:
        cart = self.cart_repo.get_or_create_user_cart(user_id)
        self.cart_repo.clear_cart(cart.id)
