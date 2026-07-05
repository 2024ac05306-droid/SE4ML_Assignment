# appointment_service.py

from fastapi import FastAPI

app = FastAPI(title="Appointment Service")

appointments = []

@app.post("/appointment")
def create_appointment(appt: dict):
    appointments.append(appt)
    return {"message": "Appointment booked"}

@app.get("/appointments")
def get_appointments():
    return appointments
