from typing import Optional
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, ValidationError
from app.core.security import generate_order_number
from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.repositories.cart_repository import CartRepository
from app.repositories.coupon_repository import CouponRepository
from app.services.cart_service import CartService


class OrderService:
    def __init__(self, db: Session):
        self.db = db
        self.order_repo = OrderRepository(db)
        self.cart_repo = CartRepository(db)
        self.coupon_repo = CouponRepository(db)
        self.cart_service = CartService(db)

    def create_order_from_cart(self, user_id: int, coupon_code: Optional[str] = None, currency: str = "USD") -> Order:
        cart_summary = self.cart_service.get_cart_summary(user_id, coupon_code=coupon_code)
        items = cart_summary["items"]
        if not items:
            raise ValidationError("Your shopping cart is empty.")

        coupon_id = None
        if coupon_code:
            coupon = self.coupon_repo.get_by_code(coupon_code)
            if coupon:
                coupon_id = coupon.id

        order_number = generate_order_number()
        order = self.order_repo.create_order(
            order_number=order_number,
            user_id=user_id,
            subtotal=cart_summary["subtotal"],
            discount=cart_summary["discount"],
            tax=cart_summary["tax"],
            total=cart_summary["total"],
            coupon_id=coupon_id,
            currency=currency
        )

        for item in items:
            price = item.course.discount_price if item.course.discount_price is not None else item.course.price
            self.order_repo.add_order_item(order_id=order.id, course_id=item.course_id, price=price)

        return order

    def get_order_by_number(self, order_number: str) -> Order:
        order = self.order_repo.get_by_order_number(order_number)
        if not order:
            raise ResourceNotFoundError("Order", order_number)
        return order
