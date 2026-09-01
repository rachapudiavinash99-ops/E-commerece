from datetime import datetime
from typing import Dict, List, Optional
from pydantic import ConfigDict, BaseModel, Field


class QuizOptionBase(BaseModel):
    option_text: str
    is_correct: bool = False
    order_index: int = 0


class QuizOptionCreate(QuizOptionBase):
    pass


class QuizOptionResponse(BaseModel):
    id: int
    question_id: int
    option_text: str
    order_index: int

    model_config = ConfigDict(from_attributes=True)


class QuizOptionAdminResponse(QuizOptionResponse):
    is_correct: bool


class QuizQuestionBase(BaseModel):
    question_text: str
    question_type: str = "single_choice"
    code_snippet: Optional[str] = None
    explanation: Optional[str] = None
    points: int = 1
    order_index: int = 0


class QuizQuestionCreate(QuizQuestionBase):
    options: List[QuizOptionBase]


class QuizQuestionResponse(QuizQuestionBase):
    id: int
    quiz_id: int
    options: List[QuizOptionResponse] = []

    model_config = ConfigDict(from_attributes=True)


class QuizBase(BaseModel):
    lesson_id: int
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    pass_percentage: int = 70
    time_limit_minutes: int = 15
    max_attempts: int = 3


class QuizCreate(QuizBase):
    questions: Optional[List[QuizQuestionCreate]] = []


class QuizResponse(QuizBase):
    id: int
    questions: List[QuizQuestionResponse] = []

    model_config = ConfigDict(from_attributes=True)


class QuizSubmitRequest(BaseModel):
    quiz_id: int
    answers: Dict[int, List[int]] # question_id -> list of selected option_ids


class QuizAttemptResponse(BaseModel):
    id: int
    quiz_id: int
    score: float
    total_points: int
    passed: bool
    correct_count: int
    total_questions: int
    completed_at: datetime
    answers_breakdown: Optional[dict] = None
