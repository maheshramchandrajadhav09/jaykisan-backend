from fastapi import FastAPI
from app.models import ScheduleResponse, ScheduleItem, InputItem, ScheduleRequest

# Create FastAPI app
app = FastAPI(
    title="Jay Kisan Backend API",
    description="हे API शेतकऱ्यांना पिकाचे schedule देण्यासाठी तयार केले आहे 🚜",
    version="1.0.0"
)

# Root endpoint (test)
@app.get("/")
def root():
    return {"message": "✅ Jay Kisan Backend चालू आहे! Swagger UI: /docs"}

# Schedule API
@app.post("/api/v1/schedule", response_model=ScheduleResponse)
def get_schedule(req: ScheduleRequest):
    """
    दिलेल्या cropId, sowingDate आणि farmingType वरून पिकाचे schedule परत करतो.
    आत्ता sample/demo data देतो.
    """
    return ScheduleResponse(
        cropId=req.cropId,
        displayName=req.cropId,
        farmingType=req.farmingType,
        schedule=[
            ScheduleItem(
                dateString="Day 1",
                task="पेरणी तयारी",
                inputs=[InputItem(name="बी-बियाणे", qty="10kg", cost=500)]
            ),
            ScheduleItem(
                dateString="Day 7",
                task="खत टाकणे",
                inputs=[InputItem(name="युरिया", qty="5kg", cost=300)]
            )
        ]
    )
