from datetime import datetime, timezone
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, AuthorizationError, ResourceConflictError
from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course import CourseCreate, CourseUpdate, CourseFilterParams
from app.utils.slugify import generate_slug


class CourseService:
    def __init__(self, db: Session):
        self.db = db
        self.course_repo = CourseRepository(db)

    def search_courses(self, params: CourseFilterParams) -> Tuple[List[Course], int]:
        return self.course_repo.search_courses(
            query=params.query,
            category_id=params.category_id,
            topic_id=params.topic_id,
            level=params.level,
            min_price=params.min_price,
            max_price=params.max_price,
            min_rating=params.min_rating,
            status="published",
            sort_by=params.sort_by,
            page=params.page,
            page_size=params.page_size
        )

    def get_course_by_slug(self, slug: str) -> Course:
        course = self.course_repo.get_by_slug(slug)
        if not course:
            raise ResourceNotFoundError("Course", slug)
        return course

    def get_course_detail(self, course_id: int) -> Course:
        course = self.course_repo.get_detail_by_id(course_id)
        if not course:
            raise ResourceNotFoundError("Course", course_id)
        return course

    def create_course(self, instructor_id: int, req: CourseCreate) -> Course:
        slug = req.slug or generate_slug(req.title)
        existing = self.course_repo.get_by_slug(slug)
        if existing:
            slug = f"{slug}-{int(datetime.now(timezone.utc).timestamp())}"

        return self.course_repo.create(
            instructor_id=instructor_id,
            topic_id=req.topic_id,
            title=req.title,
            slug=slug,
            subtitle=req.subtitle,
            description=req.description,
            short_description=req.short_description,
            price=req.price,
            discount_price=req.discount_price,
            level=req.level,
            language=req.language,
            duration_hours=req.duration_hours,
            thumbnail_url=req.thumbnail_url,
            promo_video_url=req.promo_video_url,
            requirements=req.requirements,
            what_you_will_learn=req.what_you_will_learn,
            target_audience=req.target_audience,
            status="draft"
        )

    def update_course(self, course_id: int, instructor_id: int, req: CourseUpdate, is_admin: bool = False) -> Course:
        course = self.get_course_detail(course_id)
        if course.instructor_id != instructor_id and not is_admin:
            raise AuthorizationError("You can only edit your own courses.")

        update_dict = req.model_dump(exclude_unset=True)
        return self.course_repo.update(course, **update_dict)

    def update_course_status(self, course_id: int, new_status: str) -> Course:
        course = self.get_course_detail(course_id)
        course.status = new_status
        if new_status == "published" and not course.published_at:
            course.published_at = datetime.now(timezone.utc)
        self.db.commit()
        return course
