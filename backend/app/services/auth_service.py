from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.exceptions import AuthenticationError, ResourceConflictError, ResourceNotFoundError
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_password_hash,
    verify_password,
    generate_random_token
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def register(self, req: RegisterRequest) -> TokenResponse:
        existing = self.user_repo.get_by_email(req.email)
        if existing:
            raise ResourceConflictError("A user with this email address already exists.")

        user = self.user_repo.create_user(
            email=req.email,
            password_hash=get_password_hash(req.password),
            full_name=req.full_name,
            role=req.role or "student",
            headline=req.headline,
            bio=req.bio,
            is_active=True,
            is_verified=True
        )

        self.user_repo.log_activity(user.id, "register", "Account successfully created.")
        return self._build_token_response(user)

    def login(self, req: LoginRequest, device_info: Optional[str] = None) -> TokenResponse:
        user = self.user_repo.get_by_email(req.email)
        if not user or not verify_password(req.password, user.password_hash):
            raise AuthenticationError("Invalid email address or password.")

        if not user.is_active:
            raise AuthenticationError("Account is inactive. Please contact support.")

        self.user_repo.update_last_login(user.id)
        self.user_repo.log_activity(user.id, "login", f"User logged in from {device_info or 'web'}")

        return self._build_token_response(user, device_info=device_info)

    def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        payload = decode_token(refresh_token)
        if not payload or payload.get("type") != "refresh":
            raise AuthenticationError("Invalid or expired refresh token.")

        token_record = self.user_repo.find_refresh_token(refresh_token)
        if not token_record:
            raise AuthenticationError("Refresh token has been revoked or expired.")

        user = self.user_repo.get(int(payload["sub"]))
        if not user or not user.is_active:
            raise AuthenticationError("User account not found or deactivated.")

        # Revoke old refresh token and rotate
        self.user_repo.revoke_refresh_token(refresh_token)
        return self._build_token_response(user)

    def get_current_user_from_token(self, token: str) -> User:
        payload = decode_token(token)
        if not payload or payload.get("type") != "access":
            raise AuthenticationError("Invalid authentication credentials.")

        user_id = int(payload.get("sub", 0))
        user = self.user_repo.get(user_id)
        if not user or not user.is_active:
            raise AuthenticationError("User account not found or deactivated.")
        return user

    def _build_token_response(self, user: User, device_info: Optional[str] = None) -> TokenResponse:
        access_token = create_access_token(subject=user.id, role=user.role, email=user.email)
        refresh_token = create_refresh_token(subject=user.id)

        # Persist refresh token in db
        expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        self.user_repo.save_refresh_token(
            user_id=user.id,
            token=refresh_token,
            expires_at=expires_at,
            device_info=device_info
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user_id=user.id,
            email=user.email,
            full_name=user.full_name,
            role=user.role,
            avatar_url=user.avatar_url
        )
