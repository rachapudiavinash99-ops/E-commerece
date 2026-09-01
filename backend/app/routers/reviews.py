from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_409_conflict, ResourceConflictError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewResponse
from app.schemas.common import MessageResponse
from app.services.review_service import ReviewService

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.get("/course/{course_id}", response_model=List[ReviewResponse])
def get_course_reviews(
    course_id: int,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    service = ReviewService(db)
    skip = (page - 1) * page_size
    return service.list_course_reviews(course_id, skip=skip, limit=page_size)


@router.post("", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def submit_review(
    req: ReviewCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = ReviewService(db)
    try:
        return service.submit_review(user.id, req)
    except ResourceConflictError as e:
        raise http_409_conflict(str(e.message))
