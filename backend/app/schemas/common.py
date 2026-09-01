from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool


class MessageResponse(BaseModel):
    message: str
    success: bool = True
    details: Optional[dict] = None


class StatusResponse(BaseModel):
    status: str
    code: int = 200
    timestamp: str


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    code: int = 400
