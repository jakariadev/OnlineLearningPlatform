# import pytest
# from fastapi.testclient import TestClient
# from main import app
# from database import Base, engine, SessionLocal
# from models import Base, Course, Enrollment
# from datetime import date


# from sqlalchemy import create_engine, text
# from sqlalchemy.pool import StaticPool
# from sqlalchemy.orm import sessionmaker
# from routers.courses import get_db

# # Create a TestClient instance
# client = TestClient(app)


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./testems.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)


# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# app.dependency_overrides[get_db] = override_get_db
# client = TestClient(app)

# @pytest.fixture
# def test_course():
#     course = Course(
#         title='Test Course',
#         description='This is a test course',
#         instructor='Test Instructor',
#         duration=5,
#         price=50.0,
#     )

#     db = TestingSessionLocal()
#     db.add(course)
#     db.commit()
#     yield course
#     # with engine.connect() as connection:
#     #     connection.execute(text("DELETE FROM courses;"))
#     #     connection.commit()


    
# def test_enroll_student(test_course):

#     # Define an enrollment payload
#     enrollment_payload = {
#         "student_name": "Test Student",
#         "enrollment_date": str(date.today()),
#         "course_id": {"id": test_course.course_id}
#     }
#     db = TestingSessionLocal()

#     # Send a POST request to enroll a student
#     response = client.post("/enrollments/", json=enrollment_payload)
#     assert response.status_code == 201

#     # Check if the student is enrolled in the course in the database
#     enrollment = db.query(Enrollment).filter(Enrollment.student_name == "Test Student").first()
#     # print("#######  ", enrollment)
#     # assert enrollment is not None

#     # assert enrollment.student_name == enrollment.get('student_name')