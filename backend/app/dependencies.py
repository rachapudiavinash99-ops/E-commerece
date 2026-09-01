from typing import List
from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import AuthenticationError, AuthorizationError, http_401_unauthorized, http_403_forbidden
from app.models.user import User
from app.services.auth_service import AuthService


def get_current_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
) -> User:
    if not authorization or not authorization.startswith("Bearer "):
        raise http_401_unauthorized("Missing or malformed Authorization header.")

    token = authorization.replace("Bearer ", "").strip()
    auth_service = AuthService(db)
    try:
        user = auth_service.get_current_user_from_token(token)
        return user
    except AuthenticationError as e:
        raise http_401_unauthorized(str(e.message))


def get_optional_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
) -> User | None:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    token = authorization.replace("Bearer ", "").strip()
    auth_service = AuthService(db)
    try:
        return auth_service.get_current_user_from_token(token)
    except Exception:
        return None


def require_roles(allowed_roles: List[str]):
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise http_403_forbidden(f"Access restricted. Required roles: {allowed_roles}")
        return current_user
    return role_checker
