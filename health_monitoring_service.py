# health_monitoring_service.py

from fastapi import FastAPI

app = FastAPI(title="Health Monitoring Service")

health_data = []

@app.post("/health")
def add_health_data(data: dict):
    health_data.append(data)
    return {"message": "Health data stored"}

@app.get("/health")
def get_health_data():
    return health_data
