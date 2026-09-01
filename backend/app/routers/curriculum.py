from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.lesson import LessonResponse, ModuleWithLessonsResponse
from app.services.curriculum_service import CurriculumService

router = APIRouter(prefix="/curriculum", tags=["Curriculum"])


@router.get("/courses/{course_id}", response_model=List[ModuleWithLessonsResponse])
def get_curriculum(course_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.get_course_curriculum(course_id)


@router.get("/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson_details(lesson_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.get_lesson(lesson_id)
