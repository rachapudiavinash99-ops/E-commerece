import secrets
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from app.core.exceptions import PaymentProcessingError, ResourceNotFoundError
from app.models.payment import Payment
from app.repositories.payment_repository import PaymentRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.cart_repository import CartRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.coupon_repository import CouponRepository
from app.repositories.notification_repository import NotificationRepository


class PaymentService:
    def __init__(self, db: Session):
        self.db = db
        self.payment_repo = PaymentRepository(db)
        self.order_repo = OrderRepository(db)
        self.cart_repo = CartRepository(db)
        self.enrollment_repo = EnrollmentRepository(db)
        self.coupon_repo = CouponRepository(db)
        self.notification_repo = NotificationRepository(db)

    def initiate_payment(self, order_id: int, payment_method: str = "mock_gateway") -> Payment:
        order = self.order_repo.get(order_id)
        if not order:
            raise ResourceNotFoundError("Order", order_id)

        transaction_id = f"txn_{secrets.token_hex(12)}"
        payment = self.payment_repo.create_payment(
            order_id=order.id,
            transaction_id=transaction_id,
            amount=order.total,
            currency=order.currency,
            payment_method=payment_method
        )
        self.payment_repo.log_transaction(
            payment_id=payment.id,
            event_type="payment.initiated",
            status="initiated",
            response_data={"order_id": order.id, "amount": order.total}
        )
        return payment

    def process_payment_verification(self, transaction_id: str, order_id: int, simulate_failure: bool = False) -> Payment:
        payment = self.payment_repo.get_by_transaction_id(transaction_id)
        if not payment:
            raise ResourceNotFoundError("Payment", transaction_id)

        order = self.order_repo.get(order_id)
        if not order:
            raise ResourceNotFoundError("Order", order_id)

        if simulate_failure:
            payment.status = "failed"
            order.payment_status = "failed"
            order.order_status = "failed"
            self.payment_repo.log_transaction(payment.id, "payment.failed", "failed", {"reason": "Simulated card decline"})
            self.db.commit()
            raise PaymentProcessingError("Payment authorization was declined by the test gateway.")

        payment.status = "successful"
        payment.paid_at = datetime.now(timezone.utc)
        order.payment_status = "successful"
        order.order_status = "completed"

        # Record coupon usage if applied
        if order.coupon_id:
            self.coupon_repo.record_usage(order.coupon_id, order.user_id, order.id)

        # Automatically enroll user into purchased courses
        for item in order.items:
            self.enrollment_repo.enroll(user_id=order.user_id, course_id=item.course_id, order_id=order.id)

        # Clear student cart
        cart = self.cart_repo.get_or_create_user_cart(order.user_id)
        self.cart_repo.clear_cart(cart.id)

        # Create confirmation notification
        self.notification_repo.create(
            user_id=order.user_id,
            title="Order Completed Successfully!",
            message=f"Order #{order.order_number} has been processed. You can now access your new courses!",
            notification_type="order_confirmation",
            link_url=f"/student/dashboard"
        )

        self.payment_repo.log_transaction(payment.id, "payment.success", "successful", {"order_number": order.order_number})
        self.db.commit()
        return payment
