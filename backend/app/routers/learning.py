from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_403_forbidden, CourseNotEnrolledError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.enrollment import EnrollmentResponse
from app.schemas.progress import LessonProgressUpdate, CourseLearningOverview
from app.services.learning_service import LearningService

router = APIRouter(prefix="/learning", tags=["Student Learning"])


@router.get("/enrollments", response_model=List[EnrollmentResponse])
def get_student_enrollments(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = LearningService(db)
    return service.enrollment_repo.get_user_enrollments(user.id)


@router.get("/courses/{course_id}", response_model=CourseLearningOverview)
def get_course_learning_state(
    course_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = LearningService(db)
    try:
        return service.get_course_learning_overview(user.id, course_id)
    except CourseNotEnrolledError as e:
        raise http_403_forbidden(str(e.message))


@router.post("/lessons/{lesson_id}/complete")
def complete_lesson(
    lesson_id: int,
    req: LessonProgressUpdate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = LearningService(db)
    try:
        return service.mark_lesson_complete(user.id, lesson_id, watched_seconds=req.watched_seconds)
    except CourseNotEnrolledError as e:
        raise http_403_forbidden(str(e.message))
