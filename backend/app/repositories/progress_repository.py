from datetime import datetime, timezone
from typing import List, Optional, Tuple
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.progress import LessonProgress
from app.models.lesson import Lesson
from app.models.module import Module
from app.models.enrollment import Enrollment
from app.repositories.base import BaseRepository


class ProgressRepository(BaseRepository[LessonProgress]):
    def __init__(self, db: Session):
        super().__init__(LessonProgress, db)

    def get_lesson_progress(self, user_id: int, lesson_id: int) -> Optional[LessonProgress]:
        return self.db.query(LessonProgress).filter(
            LessonProgress.user_id == user_id,
            LessonProgress.lesson_id == lesson_id
        ).first()

    def mark_lesson_complete(self, user_id: int, lesson_id: int, watched_seconds: int = 0) -> LessonProgress:
        prog = self.get_lesson_progress(user_id, lesson_id)
        if not prog:
            prog = LessonProgress(
                user_id=user_id,
                lesson_id=lesson_id,
                completed=True,
                watched_seconds=watched_seconds,
                completed_at=datetime.now(timezone.utc),
                last_accessed_at=datetime.now(timezone.utc)
            )
            self.db.add(prog)
        else:
            prog.completed = True
            prog.watched_seconds = max(prog.watched_seconds, watched_seconds)
            prog.completed_at = datetime.now(timezone.utc)
            prog.last_accessed_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(prog)
        return prog

    def calculate_course_progress(self, user_id: int, course_id: int) -> Tuple[float, int, int, List[int]]:
        total_lessons = (
            self.db.query(func.count(Lesson.id))
            .join(Module, Module.id == Lesson.module_id)
            .filter(Module.course_id == course_id, Lesson.is_published == True)
            .scalar() or 0
        )

        completed_lesson_rows = (
            self.db.query(LessonProgress.lesson_id)
            .join(Lesson, Lesson.id == LessonProgress.lesson_id)
            .join(Module, Module.id == Lesson.module_id)
            .filter(
                LessonProgress.user_id == user_id,
                LessonProgress.completed == True,
                Module.course_id == course_id
            )
            .all()
        )
        completed_ids = [r[0] for r in completed_lesson_rows]
        completed_count = len(completed_ids)

        percentage = round((completed_count / total_lessons * 100.0), 1) if total_lessons > 0 else 0.0

        enrollment = self.db.query(Enrollment).filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        ).first()
        if enrollment:
            enrollment.completion_percentage = percentage
            if percentage >= 100.0 and not enrollment.is_completed:
                enrollment.is_completed = True
                enrollment.completed_at = datetime.now(timezone.utc)
            self.db.commit()

        return percentage, completed_count, total_lessons, completed_ids
