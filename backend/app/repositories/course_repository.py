from typing import List, Optional, Tuple
from sqlalchemy import func, or_
from sqlalchemy.orm import Session, joinedload
from app.models.course import Course
from app.models.topic import Topic
from app.models.category import Category
from app.models.review import Review
from app.repositories.base import BaseRepository


class CourseRepository(BaseRepository[Course]):
    def __init__(self, db: Session):
        super().__init__(Course, db)

    def get_by_slug(self, slug: str) -> Optional[Course]:
        return (
            self.db.query(Course)
            .filter(Course.slug == slug)
            .options(
                joinedload(Course.instructor),
                joinedload(Course.topic).joinedload(Topic.category),
                joinedload(Course.modules)
            )
            .first()
        )

    def get_detail_by_id(self, course_id: int) -> Optional[Course]:
        return (
            self.db.query(Course)
            .filter(Course.id == course_id)
            .options(
                joinedload(Course.instructor),
                joinedload(Course.topic).joinedload(Topic.category),
                joinedload(Course.modules)
            )
            .first()
        )

    def search_courses(
        self,
        query: Optional[str] = None,
        category_id: Optional[int] = None,
        topic_id: Optional[int] = None,
        level: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_rating: Optional[float] = None,
        status: Optional[str] = "published",
        sort_by: Optional[str] = "popularity",
        page: int = 1,
        page_size: int = 12
    ) -> Tuple[List[Course], int]:
        q = self.db.query(Course).join(Course.topic)

        if status:
            q = q.filter(Course.status == status)

        if query:
            pattern = f"%{query}%"
            q = q.filter(
                or_(
                    Course.title.ilike(pattern),
                    Course.subtitle.ilike(pattern),
                    Course.description.ilike(pattern),
                    Topic.name.ilike(pattern)
                )
            )

        if category_id:
            q = q.filter(Topic.category_id == category_id)

        if topic_id:
            q = q.filter(Course.topic_id == topic_id)

        if level and level != "all_levels":
            q = q.filter(Course.level == level)

        if min_price is not None:
            q = q.filter(Course.price >= min_price)

        if max_price is not None:
            q = q.filter(Course.price <= max_price)

        if min_rating is not None:
            q = q.filter(Course.average_rating >= min_rating)

        if sort_by == "rating":
            q = q.order_by(Course.average_rating.desc(), Course.review_count.desc())
        elif sort_by == "price_low":
            q = q.order_by(Course.price.asc())
        elif sort_by == "price_high":
            q = q.order_by(Course.price.desc())
        elif sort_by == "newest":
            q = q.order_by(Course.created_at.desc())
        elif sort_by == "bestseller":
            q = q.order_by(Course.is_bestseller.desc(), Course.student_count.desc())
        else:
            q = q.order_by(Course.student_count.desc(), Course.average_rating.desc())

        total = q.count()
        courses = (
            q.options(
                joinedload(Course.instructor),
                joinedload(Course.topic).joinedload(Topic.category)
            )
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return courses, total

    def get_featured(self, limit: int = 8) -> List[Course]:
        return (
            self.db.query(Course)
            .filter(Course.status == "published", Course.is_featured == True)
            .options(joinedload(Course.instructor), joinedload(Course.topic))
            .limit(limit)
            .all()
        )

    def get_bestsellers(self, limit: int = 8) -> List[Course]:
        return (
            self.db.query(Course)
            .filter(Course.status == "published", Course.is_bestseller == True)
            .options(joinedload(Course.instructor), joinedload(Course.topic))
            .limit(limit)
            .all()
        )

    def get_by_instructor(self, instructor_id: int) -> List[Course]:
        return (
            self.db.query(Course)
            .filter(Course.instructor_id == instructor_id)
            .options(joinedload(Course.topic))
            .order_by(Course.updated_at.desc())
            .all()
        )

    def recalculate_rating(self, course_id: int) -> None:
        course = self.get(course_id)
        if not course:
            return
        stats = (
            self.db.query(
                func.avg(Review.rating).label("avg_rating"),
                func.count(Review.id).label("count")
            )
            .filter(Review.course_id == course_id, Review.status == "approved")
            .first()
        )
        course.average_rating = round(float(stats.avg_rating or 0.0), 1)
        course.review_count = int(stats.count or 0)
        self.db.commit()
