from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field


class TestCaseBase(BaseModel):
    input_data: Optional[str] = None
    expected_output: str
    is_hidden: bool = False
    explanation: Optional[str] = None


class TestCaseCreate(TestCaseBase):
    task_id: int


class TestCaseResponse(TestCaseBase):
    id: int
    task_id: int

    model_config = ConfigDict(from_attributes=True)


class CodingTaskBase(BaseModel):
    lesson_id: int
    title: str = Field(..., min_length=3, max_length=200)
    instructions: str
    task_type: str = Field("coding", pattern="^(coding|multiple_choice|sql|output_prediction|debugging|true_false|project)$")
    difficulty: str = "medium"
    language: str = "python"
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    hints: Optional[str] = None
    points: int = 10
    time_limit_seconds: int = 5


class CodingTaskCreate(CodingTaskBase):
    test_cases: Optional[List[TestCaseBase]] = []


class CodingTaskUpdate(BaseModel):
    title: Optional[str] = None
    instructions: Optional[str] = None
    task_type: Optional[str] = None
    difficulty: Optional[str] = None
    language: Optional[str] = None
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    hints: Optional[str] = None
    points: Optional[int] = None
    time_limit_seconds: Optional[int] = None


class CodingTaskResponse(CodingTaskBase):
    id: int
    test_cases: List[TestCaseResponse] = []

    model_config = ConfigDict(from_attributes=True)


class TaskSubmissionRequest(BaseModel):
    task_id: int
    code: str


class TaskSubmissionResponse(BaseModel):
    id: int
    task_id: int
    status: str # passed, failed, syntax_error, runtime_error, timeout
    output: Optional[str] = None
    execution_time_ms: float
    score: int
    total_points: int
    passed_test_cases: int
    total_test_cases: int
    details: Optional[str] = None
    submitted_at: datetime
