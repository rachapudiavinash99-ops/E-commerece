from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel


class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    notification_type: str
    link_url: Optional[str] = None
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
