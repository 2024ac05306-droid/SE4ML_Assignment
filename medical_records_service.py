# medical_records_service.py

from fastapi import FastAPI

app = FastAPI(title="Medical Records Service")

records = []

@app.post("/record")
def add_record(record: dict):
    records.append(record)
    return {"message": "Medical record added"}

@app.get("/records")
def get_records():
    return records
