from datetime import datetime, timezone
import json
from typing import Optional
from sqlalchemy.orm import Session
from app.models.payment import Payment, PaymentTransaction
from app.repositories.base import BaseRepository


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self, db: Session):
        super().__init__(Payment, db)

    def get_by_transaction_id(self, transaction_id: str) -> Optional[Payment]:
        return self.db.query(Payment).filter(Payment.transaction_id == transaction_id).first()

    def get_by_order_id(self, order_id: int) -> Optional[Payment]:
        return self.db.query(Payment).filter(Payment.order_id == order_id).first()

    def create_payment(
        self,
        order_id: int,
        transaction_id: str,
        amount: float,
        currency: str = "USD",
        payment_method: str = "mock_gateway"
    ) -> Payment:
        payment = Payment(
            order_id=order_id,
            transaction_id=transaction_id,
            amount=amount,
            currency=currency,
            status="initiated",
            payment_method=payment_method
        )
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def log_transaction(self, payment_id: int, event_type: str, status: str, response_data: dict) -> PaymentTransaction:
        pt = PaymentTransaction(
            payment_id=payment_id,
            event_type=event_type,
            status=status,
            response_data=json.dumps(response_data)
        )
        self.db.add(pt)
        self.db.commit()
        return pt
