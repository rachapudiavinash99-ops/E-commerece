from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field


class ModuleBase(BaseModel):
    course_id: int
    title: str = Field(..., min_length=2, max_length=200)
    description: Optional[str] = None
    order_index: int = 0
    is_published: bool = True


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    order_index: Optional[int] = None
    is_published: Optional[bool] = None


class ModuleResponse(ModuleBase):
    id: int
    lesson_count: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)
