from fastapi import FastAPI
from app.models import ScheduleRequest, ScheduleResponse
from app.sample_data import generate_sample_schedule  # schedule तयार करणारी फाइल import

app = FastAPI(
    title="Jay Kisan Backend API",
    description="हे API शेतकऱ्यांना पिकाचे schedule देण्यासाठी तयार केले आहे 🚜",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे! Swagger UI: /docs"}

# Schedule API
@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    """
    दिलेल्या cropId, sowingDate आणि farmingType वरून पिकाचे schedule तयार करतो.
    """
    return generate_sample_schedule(req.cropId, req.farmingType, req.sowingDate)
