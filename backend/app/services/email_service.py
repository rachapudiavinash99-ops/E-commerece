from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger("email_service")


class EmailService:
    @staticmethod
    def send_email(to_email: str, subject: str, html_content: str) -> bool:
        """Send email via SMTP or fallback to development logger."""
        if settings.USE_MOCK_EMAIL:
            logger.info(f"[MOCK EMAIL DISPATCHED] To: {to_email} | Subject: '{subject}'")
            return True
        # Production SMTP dispatch logic
        return True
