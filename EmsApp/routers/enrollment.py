from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path, HTTPException
from models import Course, Enrollment
from starlette import status
from pydantic import BaseModel, Field
from database import SessionLocal
from datetime import date

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


router = APIRouter(
    prefix='/enrollments',
    tags=['Enrollments']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

class CourseID(BaseModel):
    id: int


class EnrollmentRequest(BaseModel):
    student_name: str = Field(min_length=1, max_length=300)
    enrollment_date: date
    course_id: CourseID

@router.post("/", status_code=status.HTTP_201_CREATED)
def enroll_student(requested_course: EnrollmentRequest, db: Session = Depends(get_db)):
    course_id = requested_course.course_id.id
    
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    enrollment = Enrollment(student_name=requested_course.student_name,
                            enrollment_date=requested_course.enrollment_date,
                            course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    
    # Create a response object with the desired format
    response_enrollment = {
        "student_name": enrollment.student_name,
        "course": {
            "id": course.course_id,
            "title": course.title,
            "description": course.description,
            "instructor": course.instructor,
            "duration": course.duration,
            "price": course.price
        },
        "enrollment_date": enrollment.enrollment_date,
        "enrollment_id": enrollment.enrollment_id
    }
    
    return response_enrollment
