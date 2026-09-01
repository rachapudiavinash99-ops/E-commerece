from typing import List
from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.repositories.notification_repository import NotificationRepository


class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        self.notification_repo = NotificationRepository(db)

    def get_user_notifications(self, user_id: int, unread_only: bool = False) -> List[Notification]:
        return self.notification_repo.get_user_notifications(user_id, unread_only=unread_only)

    def mark_all_read(self, user_id: int) -> None:
        self.notification_repo.mark_all_as_read(user_id)
