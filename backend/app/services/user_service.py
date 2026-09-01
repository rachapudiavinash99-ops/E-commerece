from typing import Optional
from sqlalchemy.orm import Session
from app.core.exceptions import ResourceNotFoundError, AuthenticationError
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserUpdate, UserProfileResponse


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def get_profile(self, user_id: int) -> User:
        user = self.user_repo.get(user_id)
        if not user:
            raise ResourceNotFoundError("User", user_id)
        return user

    def update_profile(self, user_id: int, update_data: UserUpdate) -> User:
        user = self.get_profile(user_id)
        return self.user_repo.update(user, **update_data.model_dump(exclude_unset=True))

    def change_password(self, user_id: int, old_pass: str, new_pass: str) -> None:
        user = self.get_profile(user_id)
        if not verify_password(old_pass, user.password_hash):
            raise AuthenticationError("Current password is incorrect.")
        user.password_hash = get_password_hash(new_pass)
        self.db.commit()
