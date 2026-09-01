from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError
from app.models.task import CodingTask, TaskSubmission
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskSubmissionResponse
from app.utils.code_sandbox import SafeCodeRunner


class TaskRunnerService:
    def __init__(self, db: Session):
        self.db = db
        self.task_repo = TaskRepository(db)

    def evaluate_task(self, user_id: int, task_id: int, code: str) -> TaskSubmissionResponse:
        task = self.task_repo.get_with_test_cases(task_id)
        if not task:
            raise ResourceNotFoundError("CodingTask", task_id)

        # Prepare test cases dicts
        test_case_dicts = [
            {
                "input_data": tc.input_data,
                "expected_output": tc.expected_output,
                "is_hidden": tc.is_hidden
            }
            for tc in task.test_cases
        ]

        result = SafeCodeRunner.execute_python_code(
            code=code,
            test_cases=test_case_dicts,
            timeout_seconds=task.time_limit_seconds
        )

        submission = self.task_repo.record_submission(
            user_id=user_id,
            task_id=task_id,
            submitted_code=code,
            status=result["status"],
            output=result["output"],
            execution_time_ms=result["execution_time_ms"],
            score=result["score"]
        )

        return TaskSubmissionResponse(
            id=submission.id,
            task_id=task_id,
            status=result["status"],
            output=result["output"],
            execution_time_ms=result["execution_time_ms"],
            score=result["score"],
            total_points=task.points,
            passed_test_cases=result["passed_test_cases"],
            total_test_cases=result["total_test_cases"],
            details=result.get("details"),
            submitted_at=submission.submitted_at
        )
