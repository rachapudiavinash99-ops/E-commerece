from datetime import datetime, timezone
import json
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.quiz import Quiz, QuizQuestion, QuizOption, QuizAttempt
from app.repositories.base import BaseRepository


class QuizRepository(BaseRepository[Quiz]):
    def __init__(self, db: Session):
        super().__init__(Quiz, db)

    def get_by_lesson(self, lesson_id: int) -> List[Quiz]:
        return (
            self.db.query(Quiz)
            .filter(Quiz.lesson_id == lesson_id)
            .options(joinedload(Quiz.questions).joinedload(QuizQuestion.options))
            .all()
        )

    def get_with_questions(self, quiz_id: int) -> Optional[Quiz]:
        return (
            self.db.query(Quiz)
            .filter(Quiz.id == quiz_id)
            .options(joinedload(Quiz.questions).joinedload(QuizQuestion.options))
            .first()
        )

    def record_attempt(
        self,
        user_id: int,
        quiz_id: int,
        score: float,
        total_points: int,
        passed: bool,
        answers_dict: dict
    ) -> QuizAttempt:
        attempt = QuizAttempt(
            user_id=user_id,
            quiz_id=quiz_id,
            score=score,
            total_points=total_points,
            passed=passed,
            answers_json=json.dumps(answers_dict),
            started_at=datetime.now(timezone.utc),
            completed_at=datetime.now(timezone.utc)
        )
        self.db.add(attempt)
        self.db.commit()
        self.db.refresh(attempt)
        return attempt
