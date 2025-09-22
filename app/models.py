from pydantic import BaseModel
from typing import List, Dict, Optional

class InputItem(BaseModel):
    name: str
    qty: Optional[str] = None
    cost: Optional[float] = None

class ScheduleItem(BaseModel):
    dateMillis: int
    dateString: str
    task: str
    inputs: List[InputItem] = []

class ScheduleRequest(BaseModel):
    cropId: str
    sowingDate: int
    farmingType: str

class ScheduleResponse(BaseModel):
    cropId: str
    displayName: str
    farmingType: str
    sowingDate: int
    schedule: List[ScheduleItem]
    costEstimate: Dict[str, float]
    sources: List[str]
