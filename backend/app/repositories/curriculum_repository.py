from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.module import Module
from app.models.lesson import Lesson, LessonResource


class CurriculumRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_module(self, module_id: int) -> Optional[Module]:
        return self.db.query(Module).filter(Module.id == module_id).first()

    def get_course_curriculum(self, course_id: int) -> List[Module]:
        return (
            self.db.query(Module)
            .filter(Module.course_id == course_id)
            .options(
                joinedload(Module.lessons).joinedload(Lesson.resources),
                joinedload(Module.lessons).joinedload(Lesson.coding_tasks),
                joinedload(Module.lessons).joinedload(Lesson.quizzes)
            )
            .order_by(Module.order_index)
            .all()
        )

    def create_module(self, course_id: int, title: str, description: Optional[str] = None, order_index: int = 0) -> Module:
        mod = Module(course_id=course_id, title=title, description=description, order_index=order_index)
        self.db.add(mod)
        self.db.commit()
        self.db.refresh(mod)
        return mod

    def get_lesson(self, lesson_id: int) -> Optional[Lesson]:
        return (
            self.db.query(Lesson)
            .filter(Lesson.id == lesson_id)
            .options(
                joinedload(Lesson.resources),
                joinedload(Lesson.coding_tasks),
                joinedload(Lesson.quizzes),
                joinedload(Lesson.module)
            )
            .first()
        )

    def create_lesson(
        self,
        module_id: int,
        title: str,
        slug: str,
        lesson_type: str = "video",
        content: Optional[str] = None,
        video_url: Optional[str] = None,
        duration_minutes: int = 10,
        order_index: int = 0,
        is_preview: bool = False
    ) -> Lesson:
        lesson = Lesson(
            module_id=module_id,
            title=title,
            slug=slug,
            lesson_type=lesson_type,
            content=content,
            video_url=video_url,
            duration_minutes=duration_minutes,
            order_index=order_index,
            is_preview=is_preview
        )
        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def add_resource(self, lesson_id: int, title: str, file_url: str, resource_type: str = "pdf", size_bytes: int = 0) -> LessonResource:
        res = LessonResource(
            lesson_id=lesson_id,
            title=title,
            file_url=file_url,
            resource_type=resource_type,
            size_bytes=size_bytes
        )
        self.db.add(res)
        self.db.commit()
        self.db.refresh(res)
        return res
