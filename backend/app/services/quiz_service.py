import json
from typing import Dict, List
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError
from app.models.quiz import Quiz, QuizAttempt
from app.repositories.quiz_repository import QuizRepository
from app.schemas.quiz import QuizAttemptResponse


class QuizService:
    def __init__(self, db: Session):
        self.db = db
        self.quiz_repo = QuizRepository(db)

    def submit_quiz(self, user_id: int, quiz_id: int, user_answers: Dict[int, List[int]]) -> QuizAttemptResponse:
        quiz = self.quiz_repo.get_with_questions(quiz_id)
        if not quiz:
            raise ResourceNotFoundError("Quiz", quiz_id)

        total_questions = len(quiz.questions)
        correct_count = 0
        total_points = sum(q.points for q in quiz.questions)
        earned_points = 0
        answers_breakdown = {}

        for question in quiz.questions:
            q_id = question.id
            correct_option_ids = {opt.id for opt in question.options if opt.is_correct}
            user_selected = set(user_answers.get(q_id, []))

            is_q_correct = (correct_option_ids == user_selected)
            if is_q_correct:
                correct_count += 1
                earned_points += question.points

            answers_breakdown[q_id] = {
                "correct": is_q_correct,
                "selected": list(user_selected),
                "correct_options": list(correct_option_ids),
                "explanation": question.explanation
            }

        score_percentage = round((earned_points / total_points * 100.0), 1) if total_points > 0 else 100.0
        passed = score_percentage >= quiz.pass_percentage

        attempt = self.quiz_repo.record_attempt(
            user_id=user_id,
            quiz_id=quiz_id,
            score=score_percentage,
            total_points=total_points,
            passed=passed,
            answers_dict=answers_breakdown
        )

        return QuizAttemptResponse(
            id=attempt.id,
            quiz_id=quiz_id,
            score=score_percentage,
            total_points=total_points,
            passed=passed,
            correct_count=correct_count,
            total_questions=total_questions,
            completed_at=attempt.completed_at,
            answers_breakdown=answers_breakdown
        )
