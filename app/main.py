from fastapi import FastAPI
from app.models import ScheduleResponse, ScheduleItem, InputItem, ScheduleRequest

app = FastAPI(title="Jay Kisan Backend API", version="1.0")

@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे!"}

@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    # test data / demo
    return ScheduleResponse(
        cropId=req.cropId,
        displayName=req.cropId,
        farmingType=req.farmingType,
        schedule=[
            ScheduleItem(dateString="Day 1", task="पेरणी तयारी", inputs=[InputItem(name="बी-बियाणे", qty="10kg", cost=500)])
        ]
    )
