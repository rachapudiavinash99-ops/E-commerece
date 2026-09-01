from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.task import CodingTask, TestCase, TaskSubmission
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository[CodingTask]):
    def __init__(self, db: Session):
        super().__init__(CodingTask, db)

    def get_by_lesson(self, lesson_id: int) -> List[CodingTask]:
        return (
            self.db.query(CodingTask)
            .filter(CodingTask.lesson_id == lesson_id)
            .options(joinedload(CodingTask.test_cases))
            .all()
        )

    def get_with_test_cases(self, task_id: int) -> Optional[CodingTask]:
        return (
            self.db.query(CodingTask)
            .filter(CodingTask.id == task_id)
            .options(joinedload(CodingTask.test_cases))
            .first()
        )

    def create_task(
        self,
        lesson_id: int,
        title: str,
        instructions: str,
        task_type: str = "coding",
        difficulty: str = "medium",
        language: str = "python",
        starter_code: Optional[str] = None,
        solution_code: Optional[str] = None,
        hints: Optional[str] = None,
        points: int = 10,
        time_limit_seconds: int = 5
    ) -> CodingTask:
        task = CodingTask(
            lesson_id=lesson_id,
            title=title,
            instructions=instructions,
            task_type=task_type,
            difficulty=difficulty,
            language=language,
            starter_code=starter_code,
            solution_code=solution_code,
            hints=hints,
            points=points,
            time_limit_seconds=time_limit_seconds
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def add_test_case(self, task_id: int, input_data: Optional[str], expected_output: str, is_hidden: bool = False, explanation: Optional[str] = None) -> TestCase:
        tc = TestCase(
            task_id=task_id,
            input_data=input_data,
            expected_output=expected_output,
            is_hidden=is_hidden,
            explanation=explanation
        )
        self.db.add(tc)
        self.db.commit()
        self.db.refresh(tc)
        return tc

    def record_submission(
        self,
        user_id: int,
        task_id: int,
        submitted_code: str,
        status: str,
        output: Optional[str],
        execution_time_ms: float,
        score: int
    ) -> TaskSubmission:
        sub = TaskSubmission(
            user_id=user_id,
            task_id=task_id,
            submitted_code=submitted_code,
            status=status,
            output=output,
            execution_time_ms=execution_time_ms,
            score=score,
            submitted_at=datetime.now(timezone.utc)
        )
        self.db.add(sub)
        self.db.commit()
        self.db.refresh(sub)
        return sub
