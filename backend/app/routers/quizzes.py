from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.quiz import QuizResponse, QuizSubmitRequest, QuizAttemptResponse
from app.services.quiz_service import QuizService

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])


@router.get("/lesson/{lesson_id}", response_model=List[QuizResponse])
def get_quizzes_for_lesson(lesson_id: int, db: Session = Depends(get_db)):
    service = QuizService(db)
    return service.quiz_repo.get_by_lesson(lesson_id)


@router.post("/submit", response_model=QuizAttemptResponse)
def submit_quiz_attempt(
    req: QuizSubmitRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = QuizService(db)
    return service.submit_quiz(user_id=user.id, quiz_id=req.quiz_id, user_answers=req.answers)
