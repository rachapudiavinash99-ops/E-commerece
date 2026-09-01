from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.categories import router as categories_router
from app.routers.topics import router as topics_router
from app.routers.courses import router as courses_router
from app.routers.curriculum import router as curriculum_router
from app.routers.tasks import router as tasks_router
from app.routers.quizzes import router as quizzes_router
from app.routers.cart import router as cart_router
from app.routers.coupons import router as coupons_router
from app.routers.orders import router as orders_router
from app.routers.payments import router as payments_router
from app.routers.learning import router as learning_router
from app.routers.certificates import router as certificates_router
from app.routers.reviews import router as reviews_router
from app.routers.notifications import router as notifications_router
from app.routers.instructor import router as instructor_router
from app.routers.admin import router as admin_router

__all__ = [
    "auth_router",
    "users_router",
    "categories_router",
    "topics_router",
    "courses_router",
    "curriculum_router",
    "tasks_router",
    "quizzes_router",
    "cart_router",
    "coupons_router",
    "orders_router",
    "payments_router",
    "learning_router",
    "certificates_router",
    "reviews_router",
    "notifications_router",
    "instructor_router",
    "admin_router",
]
