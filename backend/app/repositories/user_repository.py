from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User, RefreshToken, UserActivityLog
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email.lower().strip()).first()

    def create_user(self, email: str, password_hash: str, full_name: str, role: str = "student", **kwargs) -> User:
        user = User(
            email=email.lower().strip(),
            password_hash=password_hash,
            full_name=full_name.strip(),
            role=role,
            **kwargs
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_last_login(self, user_id: int) -> None:
        user = self.get(user_id)
        if user:
            user.last_login_at = datetime.now(timezone.utc)
            self.db.commit()

    def log_activity(self, user_id: int, action: str, details: Optional[str] = None, ip_address: Optional[str] = None) -> UserActivityLog:
        log = UserActivityLog(
            user_id=user_id,
            action=action,
            details=details,
            ip_address=ip_address
        )
        self.db.add(log)
        self.db.commit()
        return log

    def save_refresh_token(self, user_id: int, token: str, expires_at: datetime, device_info: Optional[str] = None) -> RefreshToken:
        rt = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at,
            device_info=device_info
        )
        self.db.add(rt)
        self.db.commit()
        return rt

    def find_refresh_token(self, token: str) -> Optional[RefreshToken]:
        return self.db.query(RefreshToken).filter(
            RefreshToken.token == token,
            RefreshToken.is_revoked == False
        ).first()

    def revoke_refresh_token(self, token: str) -> None:
        rt = self.find_refresh_token(token)
        if rt:
            rt.is_revoked = True
            self.db.commit()
