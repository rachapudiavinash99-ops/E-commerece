from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import require_roles
from app.models.user import User
from app.schemas.user import UserProfileResponse, UserAdminUpdateRole
from app.schemas.course import CourseCardResponse, CourseStatusUpdate
from app.schemas.category import CategoryCreate, CategoryResponse
from app.schemas.topic import TopicCreate, TopicResponse
from app.schemas.coupon import CouponCreate, CouponResponse
from app.schemas.analytics import AdminOverviewAnalytics
from app.schemas.common import MessageResponse
from app.services.analytics_service import AnalyticsService
from app.services.course_service import CourseService
from app.services.category_service import CategoryService
from app.services.topic_service import TopicService
from app.services.coupon_service import CouponService

router = APIRouter(prefix="/admin", tags=["Admin Command Center"], dependencies=[Depends(require_roles(["admin"]))])


@router.get("/analytics", response_model=AdminOverviewAnalytics)
def get_admin_analytics(db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    return service.get_admin_dashboard()


@router.get("/users", response_model=List[UserProfileResponse])
def list_all_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.created_at.desc()).all()


@router.put("/users/{user_id}/role", response_model=UserProfileResponse)
def update_user_role(user_id: int, req: UserAdminUpdateRole, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.role = req.role
        if req.is_active is not None:
            user.is_active = req.is_active
        db.commit()
        db.refresh(user)
    return user


@router.put("/courses/{course_id}/status", response_model=CourseCardResponse)
def update_course_approval_status(course_id: int, req: CourseStatusUpdate, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.update_course_status(course_id, req.status)


@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(req: CategoryCreate, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.create_category(req)


@router.post("/topics", response_model=TopicResponse, status_code=status.HTTP_201_CREATED)
def create_topic(req: TopicCreate, db: Session = Depends(get_db)):
    service = TopicService(db)
    return service.create_topic(req)


@router.post("/coupons", response_model=CouponResponse, status_code=status.HTTP_201_CREATED)
def create_coupon(req: CouponCreate, db: Session = Depends(get_db)):
    service = CouponService(db)
    return service.coupon_repo.create(**req.model_dump())
