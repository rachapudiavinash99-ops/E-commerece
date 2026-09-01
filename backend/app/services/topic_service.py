from typing import List
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, ResourceConflictError
from app.models.topic import Topic
from app.repositories.topic_repository import TopicRepository
from app.schemas.topic import TopicCreate, TopicUpdate
from app.utils.slugify import generate_slug


class TopicService:
    def __init__(self, db: Session):
        self.db = db
        self.topic_repo = TopicRepository(db)

    def list_popular_topics(self, limit: int = 12) -> List[Topic]:
        return self.topic_repo.get_popular(limit=limit)

    def get_topic_by_slug(self, slug: str) -> Topic:
        t = self.topic_repo.get_by_slug(slug)
        if not t:
            raise ResourceNotFoundError("Topic", slug)
        return t

    def create_topic(self, req: TopicCreate) -> Topic:
        slug = req.slug or generate_slug(req.name)
        existing = self.topic_repo.get_by_slug(slug)
        if existing:
            raise ResourceConflictError(f"Topic slug '{slug}' already exists.")
        return self.topic_repo.create(
            category_id=req.category_id,
            name=req.name,
            slug=slug,
            description=req.description,
            icon=req.icon,
            display_order=req.display_order,
            is_popular=req.is_popular,
            is_active=req.is_active
        )
