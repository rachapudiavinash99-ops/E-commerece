from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.certificate import CertificateResponse, CertificateVerifyResponse
from app.services.certificate_service import CertificateService

router = APIRouter(prefix="/certificates", tags=["Certificates"])


@router.get("", response_model=List[CertificateResponse])
def get_my_certificates(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CertificateService(db)
    return service.cert_repo.get_user_certificates(user.id)


@router.get("/verify/{code}", response_model=CertificateVerifyResponse)
def verify_certificate_public(code: str, db: Session = Depends(get_db)):
    service = CertificateService(db)
    return service.verify_certificate(code)


@router.get("/{id}/svg")
def download_certificate_svg(id: int, db: Session = Depends(get_db)):
    service = CertificateService(db)
    cert = service.cert_repo.get(id)
    if not cert or not cert.svg_content:
        return Response(content="Certificate not found", status_code=404)
    return Response(content=cert.svg_content, media_type="image/svg+xml")
