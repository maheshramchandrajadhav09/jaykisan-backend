import os
print("📢 Starting FastAPI App")
print("📂 Current Directory:", os.getcwd())
print("📄 Files inside app/:", os.listdir(os.path.dirname(__file__)))


from fastapi import FastAPI
from app.models import ScheduleResponse, ScheduleRequest
from app.sample_data import generate_sample_schedule

app = FastAPI(
    title="Jay Kisan Backend API",
    description="🚜 हे API शेतकऱ्यांना पिकाचे schedule देण्यासाठी तयार केले आहे",
    version="1.0.0"
)

# Root endpoint (Test purpose)
@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे! Swagger UI: /docs"}

# Schedule API
@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    """
    दिलेल्या cropId, sowingDate आणि farmingType वरून पिकाचे schedule तयार करून परत करतो
    """
    return generate_sample_schedule(
        crop_id=req.cropId,
        farming_type=req.farmingType,
        sowing_date=req.sowingDate
    )
