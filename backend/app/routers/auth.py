from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, http_401_unauthorized, http_409_conflict, AuthenticationError, ResourceConflictError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, RefreshTokenRequest
from app.schemas.user import UserProfileResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        return auth_service.register(req)
    except ResourceConflictError as e:
        raise http_409_conflict(str(e.message))
    except Exception as e:
        raise http_400_bad_request(str(e))


@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, user_agent: str = Header(None), db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        return auth_service.login(req, device_info=user_agent)
    except AuthenticationError as e:
        raise http_401_unauthorized(str(e.message))


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(req: RefreshTokenRequest, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        return auth_service.refresh_access_token(req.refresh_token)
    except AuthenticationError as e:
        raise http_401_unauthorized(str(e.message))


@router.get("/me", response_model=UserProfileResponse)
def get_current_user_profile(user: User = Depends(get_current_user)):
    return user
