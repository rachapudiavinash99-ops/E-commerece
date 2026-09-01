from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.certificate import Certificate
from app.models.course import Course
from app.repositories.base import BaseRepository


class CertificateRepository(BaseRepository[Certificate]):
    def __init__(self, db: Session):
        super().__init__(Certificate, db)

    def get_by_code(self, verification_code: str) -> Optional[Certificate]:
        return (
            self.db.query(Certificate)
            .filter(Certificate.verification_code == verification_code.strip())
            .options(
                joinedload(Certificate.user),
                joinedload(Certificate.course).joinedload(Course.instructor)
            )
            .first()
        )

    def get_user_certificates(self, user_id: int) -> List[Certificate]:
        return (
            self.db.query(Certificate)
            .filter(Certificate.user_id == user_id)
            .options(
                joinedload(Certificate.course).joinedload(Course.instructor)
            )
            .order_by(Certificate.issued_at.desc())
            .all()
        )

    def get_user_course_certificate(self, user_id: int, course_id: int) -> Optional[Certificate]:
        return self.db.query(Certificate).filter(
            Certificate.user_id == user_id,
            Certificate.course_id == course_id
        ).first()
