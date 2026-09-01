from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.topic import Topic
from app.repositories.base import BaseRepository


class TopicRepository(BaseRepository[Topic]):
    def __init__(self, db: Session):
        super().__init__(Topic, db)

    def get_by_slug(self, slug: str) -> Optional[Topic]:
        return self.db.query(Topic).filter(Topic.slug == slug).options(joinedload(Topic.category)).first()

    def get_popular(self, limit: int = 12) -> List[Topic]:
        return (
            self.db.query(Topic)
            .filter(Topic.is_active == True, Topic.is_popular == True)
            .options(joinedload(Topic.category))
            .order_by(Topic.display_order)
            .limit(limit)
            .all()
        )

    def get_by_category(self, category_id: int) -> List[Topic]:
        return (
            self.db.query(Topic)
            .filter(Topic.category_id == category_id, Topic.is_active == True)
            .order_by(Topic.display_order)
            .all()
        )
