"""Application Configuration using Pydantic Settings v2.
Loads settings from environment variables and provides structured access across services.
"""
from typing import List, Optional, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central application settings and security parameters."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # General Information
    APP_NAME: str = "CodePulse Academy API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_PREFIX: str = "/api"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    # Security & JWT Tokens
    SECRET_KEY: str = "super-secret-production-grade-encryption-key-change-in-prod-32chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # Database
    DATABASE_URL: str = "sqlite:///./course_market.db"
    DB_ECHO: bool = False
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10

    # CORS & Allowed Hosts
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]
    ALLOWED_HOSTS: List[str] = ["*"]

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        return [
            "http://localhost:5173",
            "http://localhost:3000",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:3000"
        ]

    # Payment Gateway
    PAYMENT_GATEWAY_MODE: str = "sandbox"
    MOCK_PAYMENT_SUCCESS_RATE: float = 1.0
    PAYMENT_CURRENCY: str = "USD"
    PAYMENT_WEBHOOK_SECRET: str = "whsec_test_mock_webhook_secret_key_849204820"

    # Email & Notifications
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 1025
    SMTP_USER: str = "test@codepulse.io"
    SMTP_PASSWORD: str = "devpassword"
    EMAIL_FROM: str = "CodePulse Academy <no-reply@codepulse.io>"
    USE_MOCK_EMAIL: bool = True

    # Certificates
    CERTIFICATE_SIGNING_SALT: str = "codepulse-cert-crypto-salt-2026"
    CERTIFICATE_BASE_URL: str = "http://localhost:5173/certificates/verify"

    # Code Execution Sandbox
    SANDBOX_TIMEOUT_SECONDS: int = 5
    SANDBOX_MAX_MEMORY_MB: int = 128

    # Redis (Optional)
    REDIS_URL: Optional[str] = None


settings = Settings()
