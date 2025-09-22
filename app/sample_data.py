import time
from datetime import datetime, timedelta
from app.models import ScheduleItem, InputItem, ScheduleResponse

def generate_sample_schedule(crop_id: str, farming_type: str, sowing_date: int) -> ScheduleResponse:
    sow_date = datetime.fromtimestamp(sowing_date / 1000)

    # Hardcoded demo tasks
    if crop_id.lower() == "methi":
        if farming_type == "sindriya":
            tasks = [
                {"days": 7, "task": "जैविक बुरशीनाशक फवारणी",
                 "inputs": [{"name": "Trichoderma", "qty": "50g", "cost": 30}]},
                {"days": 15, "task": "वर्मी कंपोस्ट खत",
                 "inputs": [{"name": "Vermicompost", "qty": "20kg", "cost": 150}]}
            ]
        else:
            tasks = [
                {"days": 7, "task": "कार्बेन्डाझिम फवारणी",
                 "inputs": [{"name": "Carbendazim", "qty": "10g", "cost": 40}]},
                {"days": 15, "task": "युरिया टॉप ड्रेसिंग", "inputs": [{"name": "Urea", "qty": "5kg", "cost": 200}]}
            ]
    elif crop_id.lower() == "gahu":
        tasks = [
            {"days": 20, "task": "पहिली निंदणी + फवारणी",
             "inputs": [{"name": "Herbicide", "qty": "100ml", "cost": 100}]},
            {"days": 40, "task": "दुसरी खत टॉप ड्रेसिंग", "inputs": [{"name": "DAP", "qty": "10kg", "cost": 500}]}
        ]
    else:
        tasks = [{"days": 10, "task": "Demo task", "inputs": []}]

    # Convert tasks into ScheduleItem
    schedule_items = []
    total_cost = 0.0
    for t in tasks:
        date = sow_date + timedelta(days=t["days"])
        date_millis = int(date.timestamp() * 1000)
        inputs = [InputItem(**inp) for inp in t["inputs"]]
        for inp in inputs:
            if inp.cost:
                total_cost += inp.cost
        schedule_items.append(ScheduleItem(
            dateMillis=date_millis,
            dateString=date.strftime("%d/%m/%Y"),
            task=t["task"],
            inputs=inputs
        ))

    return ScheduleResponse(
        cropId=crop_id,
        displayName=crop_id.capitalize(),
        farmingType=farming_type,
        sowingDate=sowing_date,
        schedule=schedule_items,
        costEstimate={"total": total_cost},
        sources=["Sample Hardcoded Data"]
    )
