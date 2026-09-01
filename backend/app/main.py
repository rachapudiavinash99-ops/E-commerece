import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.database import create_tables
from app.core.logging import configure_logging, get_logger
from app.core.middleware import RequestLoggingAndTimingMiddleware, SecurityHeadersMiddleware
from app.core.exceptions import AppBaseException
from app.routers import (
    auth_router,
    users_router,
    categories_router,
    topics_router,
    courses_router,
    curriculum_router,
    tasks_router,
    quizzes_router,
    cart_router,
    coupons_router,
    orders_router,
    payments_router,
    learning_router,
    certificates_router,
    reviews_router,
    notifications_router,
    instructor_router,
    admin_router
)

configure_logging()
logger = get_logger("main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing CodePulse Academy platform...")
    create_tables()
    logger.info("Relational database schema ready.")
    yield
    logger.info("Shutting down CodePulse Academy platform.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
    # CodePulse Academy - Full-Stack Coding Course E-Commerce API
    High-performance, production-grade REST API backend supporting unlimited coding topics, interactive code runner tasks, shopping cart, orders, coupons, certificate verification, and role-based learning portals.
    """,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Custom Middlewares
app.add_middleware(RequestLoggingAndTimingMiddleware)
app.add_middleware(SecurityHeadersMiddleware)


@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "frontend_url": "http://localhost:5173",
        "docs_url": "http://localhost:8080/docs",
        "api_base": "http://localhost:8080/api"
    }

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppBaseException)
async def domain_exception_handler(request: Request, exc: AppBaseException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": exc.__class__.__name__, "detail": exc.message, "details": exc.details}
    )


# Health Check
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }


# Include Routers with API Prefix
api_prefix = settings.API_PREFIX
app.include_router(auth_router, prefix=api_prefix)
app.include_router(users_router, prefix=api_prefix)
app.include_router(categories_router, prefix=api_prefix)
app.include_router(topics_router, prefix=api_prefix)
app.include_router(courses_router, prefix=api_prefix)
app.include_router(curriculum_router, prefix=api_prefix)
app.include_router(tasks_router, prefix=api_prefix)
app.include_router(quizzes_router, prefix=api_prefix)
app.include_router(cart_router, prefix=api_prefix)
app.include_router(coupons_router, prefix=api_prefix)
app.include_router(orders_router, prefix=api_prefix)
app.include_router(payments_router, prefix=api_prefix)
app.include_router(learning_router, prefix=api_prefix)
app.include_router(certificates_router, prefix=api_prefix)
app.include_router(reviews_router, prefix=api_prefix)
app.include_router(notifications_router, prefix=api_prefix)
app.include_router(instructor_router, prefix=api_prefix)
app.include_router(admin_router, prefix=api_prefix)
