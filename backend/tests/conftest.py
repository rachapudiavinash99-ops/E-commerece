import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from app.core.database import SessionLocal, get_db
from app.core.security import create_access_token
from app.main import app
from app.models.user import User
from app.seeds.runner import seed_database

# Ensure database is seeded before running tests
seed_database()


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def student_auth_headers(db_session):
    user = db_session.query(User).filter(User.email == "student@codepulse.io").first()
    token = create_access_token(subject=user.id, role="student", email=user.email)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def instructor_auth_headers(db_session):
    user = db_session.query(User).filter(User.email == "guido@codepulse.io").first()
    token = create_access_token(subject=user.id, role="instructor", email=user.email)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def admin_auth_headers(db_session):
    user = db_session.query(User).filter(User.email == "admin@codepulse.io").first()
    token = create_access_token(subject=user.id, role="admin", email=user.email)
    return {"Authorization": f"Bearer {token}"}
