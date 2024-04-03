from fastapi import FastAPI
from models import Base

from database import engine
from routers import courses, enrollment


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}

url_link = "http://127.0.0.1:8000/docs"
@app.get("/")
def home_page():
    return {"status": f"Healthy! Goto: {url_link} "}

app.include_router(courses.router)
app.include_router(enrollment.router)
