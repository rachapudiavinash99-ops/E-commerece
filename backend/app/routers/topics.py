from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.topic import TopicResponse
from app.services.topic_service import TopicService

router = APIRouter(prefix="/topics", tags=["Topics"])


@router.get("/popular", response_model=List[TopicResponse])
def get_popular_topics(limit: int = 12, db: Session = Depends(get_db)):
    service = TopicService(db)
    return service.list_popular_topics(limit=limit)


@router.get("/{slug}", response_model=TopicResponse)
def get_topic_by_slug(slug: str, db: Session = Depends(get_db)):
    service = TopicService(db)
    return service.get_topic_by_slug(slug)
