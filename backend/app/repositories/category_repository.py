from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db: Session):
        super().__init__(Category, db)

    def get_by_slug(self, slug: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.slug == slug).first()

    def get_active_with_topics(self) -> List[Category]:
        return (
            self.db.query(Category)
            .filter(Category.is_active == True)
            .options(joinedload(Category.topics))
            .order_by(Category.display_order)
            .all()
        )
