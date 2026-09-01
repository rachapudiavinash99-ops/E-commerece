from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.course import CourseCardResponse
from app.schemas.user import UserPublicResponse


class CertificateResponse(BaseModel):
    id: int
    certificate_number: str
    verification_code: str
    verification_hash: str
    final_grade: float
    issued_at: datetime
    pdf_url: Optional[str] = None
    svg_content: Optional[str] = None
    course: Optional[CourseCardResponse] = None
    user: Optional[UserPublicResponse] = None

    model_config = ConfigDict(from_attributes=True)


class CertificateVerifyResponse(BaseModel):
    is_valid: bool
    certificate_number: str
    verification_code: str
    student_name: str
    course_title: str
    instructor_name: str
    issued_at: datetime
    grade: float
    message: str
