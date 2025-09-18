from fastapi import FastAPI
from app.models import ScheduleResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "JayKisan backend चालू आहे!"}
