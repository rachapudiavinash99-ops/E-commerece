from sqlalchemy.orm import Session
from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:
    def __init__(self, db: Session):
        self.db = db
        self.analytics_repo = AnalyticsRepository(db)

    def get_admin_dashboard(self) -> dict:
        return self.analytics_repo.get_admin_metrics()

    def get_instructor_dashboard(self, instructor_id: int) -> dict:
        return self.analytics_repo.get_instructor_metrics(instructor_id)

    def get_student_dashboard(self, user_id: int) -> dict:
        return self.analytics_repo.get_student_metrics(user_id)
