from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path, HTTPException
from models import Course
from starlette import status
from pydantic import BaseModel, Field
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


router = APIRouter()

router = APIRouter(
    prefix='/courses',
    tags=['Courses']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

class CourseRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    description: str = Field()
    instructor: str = Field(min_length=1, max_length=255)

    duration: int = Field(ge=0, lt=100000)
    price: float = Field(ge=0, le=100000000)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_courses(db: db_dependency, instructor_query_param: str = None, price: float = None, duration: int = None):
    filtered_result = db.query(Course)

    if instructor_query_param:
         filtered_result = filtered_result.filter(Course.instructor.ilike(f"%{instructor_query_param}%"))
    if price is not None:
        filtered_result = filtered_result.filter(Course.price == price)
    if duration is not None:
        filtered_result = filtered_result.filter(Course.duration == duration)

    return filtered_result.all()



@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_course_by_id(db: db_dependency, id: int = Path(gt=0)):

    course_model = db.query(Course).filter(Course.course_id == id).first()
    if course_model is not None:
        return course_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course not Found!')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_course(db: db_dependency, requested_course: CourseRequest):
   
    course_model = Course(**requested_course.model_dump())

    db.add(course_model)
    db.commit()
    if course_model is not None:
        return course_model

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Course not Created!')
