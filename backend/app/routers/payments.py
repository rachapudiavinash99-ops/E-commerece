from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, PaymentProcessingError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.payment import PaymentInitiateRequest, PaymentInitiateResponse, PaymentVerifyRequest, PaymentResponse
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/initiate", response_model=PaymentInitiateResponse)
def initiate_payment(
    req: PaymentInitiateRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = PaymentService(db)
    payment = service.initiate_payment(req.order_id, payment_method=req.payment_method)
    return PaymentInitiateResponse(
        transaction_id=payment.transaction_id,
        order_id=payment.order_id,
        amount=payment.amount,
        currency=payment.currency,
        status=payment.status
    )


@router.post("/verify", response_model=PaymentResponse)
def verify_payment(
    req: PaymentVerifyRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = PaymentService(db)
    try:
        return service.process_payment_verification(
            transaction_id=req.transaction_id,
            order_id=req.order_id,
            simulate_failure=req.simulate_failure
        )
    except PaymentProcessingError as e:
        raise http_400_bad_request(str(e.message))
