from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.task import CodingTaskResponse, TaskSubmissionRequest, TaskSubmissionResponse
from app.services.task_runner_service import TaskRunnerService

router = APIRouter(prefix="/tasks", tags=["Coding Tasks"])


@router.get("/lesson/{lesson_id}", response_model=List[CodingTaskResponse])
def get_tasks_for_lesson(lesson_id: int, db: Session = Depends(get_db)):
    service = TaskRunnerService(db)
    return service.task_repo.get_by_lesson(lesson_id)


@router.post("/submit", response_model=TaskSubmissionResponse)
def submit_coding_task(
    req: TaskSubmissionRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = TaskRunnerService(db)
    return service.evaluate_task(user_id=user.id, task_id=req.task_id, code=req.code)
