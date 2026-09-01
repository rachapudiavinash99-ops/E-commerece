from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from app.models.review import Review, ReviewHelpful
from app.repositories.base import BaseRepository


class ReviewRepository(BaseRepository[Review]):
    def __init__(self, db: Session):
        super().__init__(Review, db)

    def get_course_reviews(self, course_id: int, skip: int = 0, limit: int = 20) -> List[Review]:
        return (
            self.db.query(Review)
            .filter(Review.course_id == course_id, Review.status == "approved")
            .options(joinedload(Review.user))
            .order_by(Review.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_user_course_review(self, user_id: int, course_id: int) -> Optional[Review]:
        return self.db.query(Review).filter(
            Review.user_id == user_id,
            Review.course_id == course_id
        ).first()

    def vote_helpful(self, review_id: int, user_id: int, is_helpful: bool = True) -> bool:
        vote = self.db.query(ReviewHelpful).filter(
            ReviewHelpful.review_id == review_id,
            ReviewHelpful.user_id == user_id
        ).first()
        if not vote:
            vote = ReviewHelpful(review_id=review_id, user_id=user_id, is_helpful=is_helpful)
            self.db.add(vote)
            review = self.get(review_id)
            if review and is_helpful:
                review.helpful_count += 1
            self.db.commit()
            return True
        return False
