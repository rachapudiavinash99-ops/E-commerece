from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.course import CourseCardResponse, CourseDetailResponse, CourseFilterParams
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("", response_model=PaginatedResponse[CourseCardResponse])
def get_courses(
    query: Optional[str] = None,
    category_id: Optional[int] = None,
    topic_id: Optional[int] = None,
    level: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    sort_by: Optional[str] = "popularity",
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    db: Session = Depends(get_db)
):
    params = CourseFilterParams(
        query=query,
        category_id=category_id,
        topic_id=topic_id,
        level=level,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        sort_by=sort_by,
        page=page,
        page_size=page_size
    )
    service = CourseService(db)
    courses, total = service.search_courses(params)
    total_pages = (total + page_size - 1) // page_size if total > 0 else 1

    return PaginatedResponse(
        items=courses,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        has_next=(page < total_pages),
        has_prev=(page > 1)
    )


@router.get("/featured", response_model=List[CourseCardResponse])
def get_featured_courses(limit: int = 8, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.course_repo.get_featured(limit=limit)


@router.get("/bestsellers", response_model=List[CourseCardResponse])
def get_bestseller_courses(limit: int = 8, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.course_repo.get_bestsellers(limit=limit)


@router.get("/{slug}", response_model=CourseDetailResponse)
def get_course_by_slug(slug: str, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.get_course_by_slug(slug)
