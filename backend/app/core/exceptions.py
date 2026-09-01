"""Custom application exception hierarchy and FastAPI error handler utilities."""
from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class AppBaseException(Exception):
    """Base class for all business domain exceptions."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationError(AppBaseException):
    """Raised when user authentication fails."""
    pass


class AuthorizationError(AppBaseException):
    """Raised when user lacks permission for an operation."""
    pass


class ResourceNotFoundError(AppBaseException):
    """Raised when requested entity is not found in database."""
    def __init__(self, resource_name: str, resource_id: Any):
        self.resource_name = resource_name
        self.resource_id = resource_id
        super().__init__(f"{resource_name} with identifier '{resource_id}' was not found.")


class ResourceConflictError(AppBaseException):
    """Raised when entity violates unique constraints or business rules."""
    pass


class ValidationError(AppBaseException):
    """Raised when user input violates domain validation rules."""
    pass


class PaymentProcessingError(AppBaseException):
    """Raised when payment gateway transaction fails."""
    pass


class CouponValidationError(AppBaseException):
    """Raised when coupon is invalid, expired, or threshold not met."""
    pass


class TaskExecutionError(AppBaseException):
    """Raised when code sandbox execution encounters an unrecoverable failure."""
    pass


class CourseNotEnrolledError(AppBaseException):
    """Raised when student tries to access non-enrolled course curriculum."""
    def __init__(self, course_id: int):
        super().__init__(f"User is not enrolled in course #{course_id}.")


def http_400_bad_request(detail: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


def http_401_unauthorized(detail: str = "Could not validate credentials") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"}
    )


def http_403_forbidden(detail: str = "You do not have permission to perform this action") -> HTTPException:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


def http_404_not_found(detail: str = "Resource not found") -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


def http_409_conflict(detail: str = "Resource already exists or conflicting state") -> HTTPException:
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)


def http_422_unprocessable(detail: str = "Unprocessable entity payload") -> HTTPException:
    return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
