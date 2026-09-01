from typing import List
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, AuthorizationError
from app.models.module import Module
from app.models.lesson import Lesson, LessonResource
from app.repositories.curriculum_repository import CurriculumRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.module import ModuleCreate, ModuleUpdate
from app.schemas.lesson import LessonCreate, LessonUpdate
from app.utils.slugify import generate_slug


class CurriculumService:
    def __init__(self, db: Session):
        self.db = db
        self.curriculum_repo = CurriculumRepository(db)
        self.course_repo = CourseRepository(db)

    def get_course_curriculum(self, course_id: int) -> List[Module]:
        return self.curriculum_repo.get_course_curriculum(course_id)

    def create_module(self, course_id: int, req: ModuleCreate) -> Module:
        return self.curriculum_repo.create_module(
            course_id=course_id,
            title=req.title,
            description=req.description,
            order_index=req.order_index
        )

    def create_lesson(self, module_id: int, req: LessonCreate) -> Lesson:
        slug = req.slug or generate_slug(req.title)
        return self.curriculum_repo.create_lesson(
            module_id=module_id,
            title=req.title,
            slug=slug,
            lesson_type=req.lesson_type,
            content=req.content,
            video_url=req.video_url,
            duration_minutes=req.duration_minutes,
            order_index=req.order_index,
            is_preview=req.is_preview
        )

    def get_lesson(self, lesson_id: int) -> Lesson:
        lesson = self.curriculum_repo.get_lesson(lesson_id)
        if not lesson:
            raise ResourceNotFoundError("Lesson", lesson_id)
        return lesson
