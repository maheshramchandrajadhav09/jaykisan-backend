from fastapi import FastAPI
from app.models import ScheduleResponse, ScheduleItem, InputItem, ScheduleRequest

app = FastAPI(
    title="Jay Kisan Backend API",
    description="हे API शेतकऱ्यांना पिकाचे schedule देण्यासाठी तयार केले आहे 🚜",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे! Swagger UI: /docs"}

@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    return ScheduleResponse(
        cropId=req.cropId,
        displayName=req.cropId,
        farmingType=req.farmingType,
        sowingDate=req.sowingDate,
        schedule=[
            ScheduleItem(
                dateMillis=req.sowingDate,
                dateString="Day 1",
                task="पेरणी तयारी",
                inputs=[InputItem(name="बी-बियाणे", qty="10kg", cost=500)]
            )
        ],
        costEstimate={"total": 500},
        sources=["Sample data"]
    )
