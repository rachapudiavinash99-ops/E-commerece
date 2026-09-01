from datetime import datetime, timezone
from typing import List, Tuple
from sqlalchemy.orm import Session
from app.core.exceptions import CourseNotEnrolledError, ResourceNotFoundError
from app.models.course import Course
from app.models.progress import LessonProgress
from app.repositories.course_repository import CourseRepository
from app.repositories.curriculum_repository import CurriculumRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.progress_repository import ProgressRepository
from app.schemas.progress import CourseLearningOverview
from app.services.certificate_service import CertificateService


class LearningService:
    def __init__(self, db: Session):
        self.db = db
        self.course_repo = CourseRepository(db)
        self.curriculum_repo = CurriculumRepository(db)
        self.enrollment_repo = EnrollmentRepository(db)
        self.progress_repo = ProgressRepository(db)
        self.cert_service = CertificateService(db)

    def verify_student_access(self, user_id: int, course_id: int) -> None:
        enrollment = self.enrollment_repo.get_enrollment(user_id, course_id)
        if not enrollment:
            raise CourseNotEnrolledError(course_id)

    def get_course_learning_overview(self, user_id: int, course_id: int) -> CourseLearningOverview:
        self.verify_student_access(user_id, course_id)
        percentage, completed_count, total_lessons, completed_ids = self.progress_repo.calculate_course_progress(user_id, course_id)

        # Check if certificate exists
        cert = self.cert_service.cert_repo.get_user_course_certificate(user_id, course_id)

        return CourseLearningOverview(
            course_id=course_id,
            completion_percentage=percentage,
            is_completed=(percentage >= 100.0),
            completed_lessons_count=completed_count,
            total_lessons_count=total_lessons,
            completed_lesson_ids=completed_ids,
            certificate_id=cert.id if cert else None
        )

    def mark_lesson_complete(self, user_id: int, lesson_id: int, watched_seconds: int = 0) -> dict:
        lesson = self.curriculum_repo.get_lesson(lesson_id)
        if not lesson:
            raise ResourceNotFoundError("Lesson", lesson_id)

        course_id = lesson.module.course_id
        self.verify_student_access(user_id, course_id)

        # Mark progress
        self.progress_repo.mark_lesson_complete(user_id, lesson_id, watched_seconds=watched_seconds)
        overview = self.get_course_learning_overview(user_id, course_id)

        # If 100% completed, automatically generate Certificate!
        if overview.is_completed:
            self.cert_service.generate_course_certificate(user_id, course_id)

        return overview.model_dump()
