import hashlib
import hmac
import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Union
from jose import JWTError, jwt
from app.core.config import settings


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a raw password against its stored cryptographic hash."""
    if not plain_password or not hashed_password:
        return False
    try:
        if hashed_password.startswith("pbkdf2:"):
            parts = hashed_password.split("$")
            if len(parts) == 3:
                salt = parts[1]
                expected_hash = parts[2]
                computed_hash = hashlib.pbkdf2_hmac("sha256", plain_password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()
                return hmac.compare_digest(expected_hash, computed_hash)
        # Fallback SHA256 with salt
        salt = settings.SECRET_KEY[:16]
        expected = hashlib.sha256(f"{salt}{plain_password}".encode("utf-8")).hexdigest()
        return hmac.compare_digest(expected, hashed_password)
    except Exception:
        return False


def get_password_hash(password: str) -> str:
    """Generate a secure PBKDF2-SHA256 cryptographic hash for a plaintext password."""
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()
    return f"pbkdf2:${salt}${key}"


def create_access_token(
    subject: Union[str, Any],
    role: str,
    email: str,
    expires_delta: Optional[timedelta] = None
) -> str:
    """Create a signed JWT access token containing subject identity and claims."""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode: Dict[str, Any] = {
        "sub": str(subject),
        "email": email,
        "role": role,
        "type": "access",
        "exp": expire,
        "iat": datetime.now(timezone.utc),
        "jti": secrets.token_hex(16)
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(
    subject: Union[str, Any],
    expires_delta: Optional[timedelta] = None
) -> str:
    """Create a signed long-lived JWT refresh token."""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode: Dict[str, Any] = {
        "sub": str(subject),
        "type": "refresh",
        "exp": expire,
        "iat": datetime.now(timezone.utc),
        "jti": secrets.token_hex(20)
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[Dict[str, Any]]:
    """Decode and validate a signed JWT token payload."""
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None


def generate_random_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def generate_order_number() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    random_suffix = secrets.token_hex(4).upper()
    return f"CP-{timestamp}-{random_suffix}"


def generate_certificate_code() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m")
    unique_suffix = secrets.token_hex(5).upper()
    return f"CERT-CP-{timestamp}-{unique_suffix}"
