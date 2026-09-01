from typing import List
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, ResourceConflictError
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.utils.slugify import generate_slug


class CategoryService:
    def __init__(self, db: Session):
        self.db = db
        self.category_repo = CategoryRepository(db)

    def list_categories_with_topics(self) -> List[Category]:
        return self.category_repo.get_active_with_topics()

    def get_category_by_id(self, cat_id: int) -> Category:
        cat = self.category_repo.get(cat_id)
        if not cat:
            raise ResourceNotFoundError("Category", cat_id)
        return cat

    def create_category(self, req: CategoryCreate) -> Category:
        slug = req.slug or generate_slug(req.name)
        existing = self.category_repo.get_by_slug(slug)
        if existing:
            raise ResourceConflictError(f"Category slug '{slug}' already exists.")
        return self.category_repo.create(
            name=req.name,
            slug=slug,
            description=req.description,
            icon=req.icon,
            image_url=req.image_url,
            display_order=req.display_order,
            is_active=req.is_active
        )
