from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models.user import User
from app.schemas.course import CourseCreate, CourseUpdate, CourseCardResponse, CourseDetailResponse
from app.schemas.module import ModuleCreate, ModuleResponse
from app.schemas.lesson import LessonCreate, LessonResponse
from app.schemas.task import CodingTaskCreate, CodingTaskResponse
from app.schemas.quiz import QuizCreate, QuizResponse
from app.schemas.analytics import InstructorOverviewAnalytics
from app.services.course_service import CourseService
from app.services.curriculum_service import CurriculumService
from app.services.task_runner_service import TaskRunnerService
from app.services.quiz_service import QuizService
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/instructor", tags=["Instructor Studio"], dependencies=[Depends(require_roles(["instructor", "admin"]))])


@router.get("/analytics", response_model=InstructorOverviewAnalytics)
def get_instructor_analytics(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    return service.get_instructor_dashboard(user.id)


@router.get("/courses", response_model=List[CourseCardResponse])
def get_instructor_courses(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.course_repo.get_by_instructor(user.id)


@router.post("/courses", response_model=CourseDetailResponse, status_code=status.HTTP_201_CREATED)
def create_course(req: CourseCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.create_course(instructor_id=user.id, req=req)


@router.put("/courses/{course_id}", response_model=CourseDetailResponse)
def update_course(course_id: int, req: CourseUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.update_course(course_id=course_id, instructor_id=user.id, req=req)


@router.post("/courses/{course_id}/modules", response_model=ModuleResponse, status_code=status.HTTP_201_CREATED)
def create_module(course_id: int, req: ModuleCreate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.create_module(course_id=course_id, req=req)


@router.post("/modules/{module_id}/lessons", response_model=LessonResponse, status_code=status.HTTP_201_CREATED)
def create_lesson(module_id: int, req: LessonCreate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.create_lesson(module_id=module_id, req=req)


@router.post("/lessons/{lesson_id}/tasks", response_model=CodingTaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(lesson_id: int, req: CodingTaskCreate, db: Session = Depends(get_db)):
    service = TaskRunnerService(db)
    task = service.task_repo.create_task(
        lesson_id=lesson_id,
        title=req.title,
        instructions=req.instructions,
        task_type=req.task_type,
        difficulty=req.difficulty,
        language=req.language,
        starter_code=req.starter_code,
        solution_code=req.solution_code,
        hints=req.hints,
        points=req.points,
        time_limit_seconds=req.time_limit_seconds
    )
    for tc in req.test_cases:
        service.task_repo.add_test_case(
            task_id=task.id,
            input_data=tc.input_data,
            expected_output=tc.expected_output,
            is_hidden=tc.is_hidden,
            explanation=tc.explanation
        )
    return service.task_repo.get_with_test_cases(task.id)
