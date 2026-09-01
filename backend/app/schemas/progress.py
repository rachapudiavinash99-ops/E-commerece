from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class LessonProgressUpdate(BaseModel):
    completed: bool = True
    watched_seconds: int = 0


class LessonProgressResponse(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    completed: bool
    watched_seconds: int
    completed_at: Optional[datetime] = None
    last_accessed_at: datetime

    class Config:
        from_attributes = True


class CourseLearningOverview(BaseModel):
    course_id: int
    completion_percentage: float
    is_completed: bool
    completed_lessons_count: int
    total_lessons_count: int
    completed_lesson_ids: List[int]
    current_lesson_id: Optional[int] = None
    certificate_id: Optional[int] = None
