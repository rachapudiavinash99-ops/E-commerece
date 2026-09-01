from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, ValidationError
from app.core.security import generate_certificate_code
from app.models.certificate import Certificate
from app.repositories.certificate_repository import CertificateRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.user_repository import UserRepository
from app.repositories.notification_repository import NotificationRepository
from app.schemas.certificate import CertificateVerifyResponse
from app.utils.certificate_generator import generate_certificate_svg
from app.utils.crypto import generate_certificate_hash


class CertificateService:
    def __init__(self, db: Session):
        self.db = db
        self.cert_repo = CertificateRepository(db)
        self.course_repo = CourseRepository(db)
        self.user_repo = UserRepository(db)
        self.notification_repo = NotificationRepository(db)

    def generate_course_certificate(self, user_id: int, course_id: int, grade: float = 100.0) -> Certificate:
        existing = self.cert_repo.get_user_course_certificate(user_id, course_id)
        if existing:
            return existing

        user = self.user_repo.get(user_id)
        course = self.course_repo.get_detail_by_id(course_id)
        if not user or not course:
            raise ResourceNotFoundError("Course or User", course_id)

        cert_code = generate_certificate_code()
        issue_date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")
        cert_hash = generate_certificate_hash(user.full_name, course.title, cert_code, issue_date_str)

        svg_content = generate_certificate_svg(
            student_name=user.full_name,
            course_title=course.title,
            instructor_name=course.instructor.full_name if course.instructor else "CodePulse Faculty",
            cert_code=cert_code,
            issue_date=issue_date_str,
            grade=grade
        )

        cert = Certificate(
            user_id=user_id,
            course_id=course_id,
            certificate_number=cert_code,
            verification_code=cert_code,
            verification_hash=cert_hash,
            final_grade=grade,
            issued_at=datetime.now(timezone.utc),
            svg_content=svg_content
        )
        self.db.add(cert)
        self.db.commit()
        self.db.refresh(cert)

        self.notification_repo.create(
            user_id=user_id,
            title="Congratulations! Certificate Earned!",
            message=f"You have earned your verified certificate for {course.title}!",
            notification_type="certificate_issued",
            link_url=f"/certificates/verify/{cert_code}"
        )
        return cert

    def verify_certificate(self, code: str) -> CertificateVerifyResponse:
        cert = self.cert_repo.get_by_code(code)
        if not cert:
            return CertificateVerifyResponse(
                is_valid=False,
                certificate_number=code,
                verification_code=code,
                student_name="Unknown",
                course_title="Unknown",
                instructor_name="Unknown",
                issued_at=datetime.now(timezone.utc),
                grade=0.0,
                message="Invalid or unrecognized certificate code."
            )

        return CertificateVerifyResponse(
            is_valid=True,
            certificate_number=cert.certificate_number,
            verification_code=cert.verification_code,
            student_name=cert.user.full_name,
            course_title=cert.course.title,
            instructor_name=cert.course.instructor.full_name if cert.course.instructor else "CodePulse Faculty",
            issued_at=cert.issued_at,
            grade=cert.final_grade,
            message="Certificate is authentic and verified by CodePulse Academy registry."
        )
