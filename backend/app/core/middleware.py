"""HTTP custom middleware for security headers, latency tracking, and request correlation."""
import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from app.core.logging import get_logger

logger = get_logger("middleware")


class RequestLoggingAndTimingMiddleware(BaseHTTPMiddleware):
    """Log incoming requests with latency and inject X-Request-ID and X-Response-Time headers."""
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        start_time = time.perf_counter()

        response = await call_next(request)

        process_time = time.perf_counter() - start_time
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time"] = f"{process_time:.4f}s"

        if request.url.path not in ["/health", "/docs", "/openapi.json"]:
            logger.info(
                f"{request.method} {request.url.path} -> {response.status_code} "
                f"({process_time * 1000:.1f}ms) [ID: {request_id[:8]}]"
            )

        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Enforce defense-in-depth HTTP security headers."""
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response
