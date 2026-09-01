from typing import List, Optional
from pydantic import BaseModel, Field


class LessonResourceBase(BaseModel):
    lesson_id: int
    title: str = Field(..., min_length=2, max_length=200)
    file_url: str
    resource_type: str = "pdf"
    size_bytes: int = 0


class LessonResourceCreate(LessonResourceBase):
    pass


class LessonResourceResponse(LessonResourceBase):
    id: int

    class Config:
        from_attributes = True


class LessonBase(BaseModel):
    module_id: int
    title: str = Field(..., min_length=2, max_length=200)
    slug: str = Field(..., min_length=2, max_length=220)
    lesson_type: str = Field("video", pattern="^(video|article|coding_task|quiz)$")
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration_minutes: int = 10
    order_index: int = 0
    is_preview: bool = False
    is_published: bool = True


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    lesson_type: Optional[str] = None
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration_minutes: Optional[int] = None
    order_index: Optional[int] = None
    is_preview: Optional[bool] = None
    is_published: Optional[bool] = None


class LessonResponse(LessonBase):
    id: int
    resources: List[LessonResourceResponse] = []

    class Config:
        from_attributes = True


class ModuleWithLessonsResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: Optional[str] = None
    order_index: int
    is_published: bool
    lessons: List[LessonResponse] = []

    class Config:
        from_attributes = True
