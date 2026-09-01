from typing import List
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceConflictError, ResourceNotFoundError
from app.models.review import Review
from app.repositories.review_repository import ReviewRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.schemas.review import ReviewCreate, ReviewUpdate


class ReviewService:
    def __init__(self, db: Session):
        self.db = db
        self.review_repo = ReviewRepository(db)
        self.course_repo = CourseRepository(db)
        self.enrollment_repo = EnrollmentRepository(db)

    def submit_review(self, user_id: int, req: ReviewCreate) -> Review:
        # Check if already reviewed
        existing = self.review_repo.get_user_course_review(user_id, req.course_id)
        if existing:
            raise ResourceConflictError("You have already reviewed this course.")

        is_verified = bool(self.enrollment_repo.get_enrollment(user_id, req.course_id))

        review = self.review_repo.create(
            user_id=user_id,
            course_id=req.course_id,
            rating=req.rating,
            title=req.title,
            comment=req.comment,
            is_verified_purchase=is_verified,
            status="approved"
        )
        # Update course average rating
        self.course_repo.recalculate_rating(req.course_id)
        return review

    def list_course_reviews(self, course_id: int, skip: int = 0, limit: int = 20) -> List[Review]:
        return self.review_repo.get_course_reviews(course_id, skip=skip, limit=limit)
