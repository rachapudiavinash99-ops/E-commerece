from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.order import Order, OrderItem
from app.models.course import Course
from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository[Order]):
    def __init__(self, db: Session):
        super().__init__(Order, db)

    def get_by_order_number(self, order_number: str) -> Optional[Order]:
        return (
            self.db.query(Order)
            .filter(Order.order_number == order_number)
            .options(
                joinedload(Order.items).joinedload(OrderItem.course).joinedload(Course.instructor),
                joinedload(Order.payment),
                joinedload(Order.user)
            )
            .first()
        )

    def get_user_orders(self, user_id: int) -> List[Order]:
        return (
            self.db.query(Order)
            .filter(Order.user_id == user_id)
            .options(joinedload(Order.items).joinedload(OrderItem.course))
            .order_by(Order.created_at.desc())
            .all()
        )

    def create_order(
        self,
        order_number: str,
        user_id: int,
        subtotal: float,
        discount: float,
        tax: float,
        total: float,
        coupon_id: Optional[int] = None,
        currency: str = "USD"
    ) -> Order:
        order = Order(
            order_number=order_number,
            user_id=user_id,
            subtotal=subtotal,
            discount=discount,
            tax=tax,
            total=total,
            coupon_id=coupon_id,
            currency=currency,
            order_status="pending",
            payment_status="initiated"
        )
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def add_order_item(self, order_id: int, course_id: int, price: float) -> OrderItem:
        item = OrderItem(order_id=order_id, course_id=course_id, price=price)
        self.db.add(item)
        self.db.commit()
        return item
