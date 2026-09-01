from typing import Dict, List, Optional
from pydantic import BaseModel


class TimeSeriesDataPoint(BaseModel):
    date: str
    value: float
    count: int = 0


class AdminOverviewAnalytics(BaseModel):
    total_users: int
    total_students: int
    total_instructors: int
    total_courses: int
    published_courses: int
    pending_approvals: int
    total_orders: int
    total_revenue: float
    total_enrollments: int
    completed_enrollments: int
    recent_revenue_trend: List[TimeSeriesDataPoint] = []
    top_selling_courses: List[dict] = []
    popular_topics: List[dict] = []


class InstructorOverviewAnalytics(BaseModel):
    total_courses: int
    published_courses: int
    draft_courses: int
    total_students: int
    total_revenue: float
    average_rating: float
    total_reviews: int
    recent_earnings: List[TimeSeriesDataPoint] = []
    course_performance: List[dict] = []


class StudentOverviewAnalytics(BaseModel):
    total_enrolled: int
    in_progress: int
    completed_courses: int
    certificates_earned: int
    total_hours_learned: float
    recent_activity: List[dict] = []
