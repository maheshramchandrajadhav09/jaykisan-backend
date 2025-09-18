# FastAPI backend साठी Dockerfile
FROM python:3.11-slim

# Workdir सेट कर
WORKDIR /app

# dependencies install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# उर्वरित कोड कॉपी कर
COPY . .

# uvicorn ने run करायचं
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
