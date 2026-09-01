from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.enrollment import Enrollment
from app.models.course import Course
from app.repositories.base import BaseRepository


class EnrollmentRepository(BaseRepository[Enrollment]):
    def __init__(self, db: Session):
        super().__init__(Enrollment, db)

    def get_user_enrollments(self, user_id: int) -> List[Enrollment]:
        return (
            self.db.query(Enrollment)
            .filter(Enrollment.user_id == user_id)
            .options(
                joinedload(Enrollment.course).joinedload(Course.instructor),
                joinedload(Enrollment.course).joinedload(Course.topic)
            )
            .order_by(Enrollment.last_accessed_at.desc())
            .all()
        )

    def get_enrollment(self, user_id: int, course_id: int) -> Optional[Enrollment]:
        return (
            self.db.query(Enrollment)
            .filter(Enrollment.user_id == user_id, Enrollment.course_id == course_id)
            .options(joinedload(Enrollment.course))
            .first()
        )

    def enroll(self, user_id: int, course_id: int, order_id: Optional[int] = None) -> Enrollment:
        existing = self.get_enrollment(user_id, course_id)
        if existing:
            return existing
        enr = Enrollment(
            user_id=user_id,
            course_id=course_id,
            order_id=order_id,
            enrolled_at=datetime.now(timezone.utc),
            completion_percentage=0.0,
            is_completed=False,
            last_accessed_at=datetime.now(timezone.utc)
        )
        self.db.add(enr)
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if course:
            course.student_count += 1
        self.db.commit()
        self.db.refresh(enr)
        return enr
