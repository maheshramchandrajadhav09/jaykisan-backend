# FastAPI backend साठी Dockerfile
FROM python:3.11-slim

WORKDIR /app

# dependencies install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# run uvicorn server on port 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
