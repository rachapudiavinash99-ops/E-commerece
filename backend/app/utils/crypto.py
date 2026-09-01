import hashlib
import hmac
from app.core.config import settings


def generate_certificate_hash(student_name: str, course_title: str, cert_code: str, issue_date: str) -> str:
    """Generate HMAC SHA-256 cryptographic verification digest."""
    message = f"{student_name}|{course_title}|{cert_code}|{issue_date}".encode("utf-8")
    key = settings.CERTIFICATE_SIGNING_SALT.encode("utf-8")
    return hmac.new(key, message, hashlib.sha256).hexdigest()
