from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    instructor = Column(String(255))
    duration = Column(Integer)
    price = Column(Float)

    # Define the relationship with Enrollment
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(Integer, primary_key=True)
    student_name = Column(String(255))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    enrollment_date = Column(Date)

    course = relationship("Course", back_populates="enrollments")
