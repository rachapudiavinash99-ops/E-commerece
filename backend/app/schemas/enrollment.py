from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.course import CourseCardResponse


class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime
    completion_percentage: float
    is_completed: bool
    completed_at: Optional[datetime] = None
    last_accessed_at: datetime
    course: CourseCardResponse

    model_config = ConfigDict(from_attributes=True)
