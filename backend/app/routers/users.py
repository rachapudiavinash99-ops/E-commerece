from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import http_400_bad_request, http_401_unauthorized, AuthenticationError
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.common import MessageResponse
from app.schemas.auth import ChangePasswordRequest
from app.schemas.user import UserUpdate, UserProfileResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile", response_model=UserProfileResponse)
def get_profile(user: User = Depends(get_current_user)):
    return user


@router.put("/profile", response_model=UserProfileResponse)
def update_profile(req: UserUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.update_profile(user.id, req)


@router.post("/change-password", response_model=MessageResponse)
def change_password(req: ChangePasswordRequest, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    try:
        user_service.change_password(user.id, req.old_password, req.new_password)
        return MessageResponse(message="Password changed successfully.")
    except AuthenticationError as e:
        raise http_401_unauthorized(str(e.message))
