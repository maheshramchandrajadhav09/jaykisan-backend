from fastapi import FastAPI
from app.models import ScheduleRequest, ScheduleResponse
from app.sample_data import generate_sample_schedule

app = FastAPI(
    title="Jay Kisan Backend API",
    description="🚜 API शेतकऱ्यांना पिकाचे schedule देण्यासाठी तयार केले आहे 🌱",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे! Swagger UI: /docs"}

@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    return generate_sample_schedule(req.cropId, req.farmingType, req.sowingDate)
