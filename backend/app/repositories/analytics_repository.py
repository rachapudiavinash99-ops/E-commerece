from typing import Dict, List, Tuple
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.course import Course
from app.models.order import Order
from app.models.enrollment import Enrollment
from app.models.certificate import Certificate


class AnalyticsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_admin_metrics(self) -> dict:
        total_users = self.db.query(func.count(User.id)).scalar() or 0
        total_students = self.db.query(func.count(User.id)).filter(User.role == "student").scalar() or 0
        total_instructors = self.db.query(func.count(User.id)).filter(User.role == "instructor").scalar() or 0
        total_courses = self.db.query(func.count(Course.id)).scalar() or 0
        published_courses = self.db.query(func.count(Course.id)).filter(Course.status == "published").scalar() or 0
        pending_approvals = self.db.query(func.count(Course.id)).filter(Course.status == "pending_approval").scalar() or 0
        total_orders = self.db.query(func.count(Order.id)).filter(Order.order_status == "completed").scalar() or 0
        total_revenue = self.db.query(func.sum(Order.total)).filter(Order.order_status == "completed").scalar() or 0.0
        total_enrollments = self.db.query(func.count(Enrollment.id)).scalar() or 0
        completed_enrollments = self.db.query(func.count(Enrollment.id)).filter(Enrollment.is_completed == True).scalar() or 0

        return {
            "total_users": total_users,
            "total_students": total_students,
            "total_instructors": total_instructors,
            "total_courses": total_courses,
            "published_courses": published_courses,
            "pending_approvals": pending_approvals,
            "total_orders": total_orders,
            "total_revenue": round(float(total_revenue), 2),
            "total_enrollments": total_enrollments,
            "completed_enrollments": completed_enrollments
        }

    def get_instructor_metrics(self, instructor_id: int) -> dict:
        courses = self.db.query(Course).filter(Course.instructor_id == instructor_id).all()
        total_courses = len(courses)
        published_courses = sum(1 for c in courses if c.status == "published")
        draft_courses = sum(1 for c in courses if c.status == "draft")
        total_students = sum(c.student_count for c in courses)
        ratings = [c.average_rating for c in courses if c.average_rating > 0]
        avg_rating = round(sum(ratings) / len(ratings), 1) if ratings else 5.0
        total_reviews = sum(c.review_count for c in courses)

        total_revenue = 0.0
        for c in courses:
            total_revenue += c.student_count * (c.discount_price if c.discount_price else c.price)

        return {
            "total_courses": total_courses,
            "published_courses": published_courses,
            "draft_courses": draft_courses,
            "total_students": total_students,
            "total_revenue": round(float(total_revenue), 2),
            "average_rating": avg_rating,
            "total_reviews": total_reviews
        }

    def get_student_metrics(self, user_id: int) -> dict:
        enrollments = self.db.query(Enrollment).filter(Enrollment.user_id == user_id).all()
        total_enrolled = len(enrollments)
        completed_courses = sum(1 for e in enrollments if e.is_completed)
        in_progress = total_enrolled - completed_courses
        certificates_count = self.db.query(func.count(Certificate.id)).filter(Certificate.user_id == user_id).scalar() or 0

        return {
            "total_enrolled": total_enrolled,
            "in_progress": in_progress,
            "completed_courses": completed_courses,
            "certificates_earned": certificates_count,
            "total_hours_learned": round(total_enrolled * 4.5, 1)
        }
