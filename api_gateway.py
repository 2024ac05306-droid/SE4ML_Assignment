# api_gateway.py

from fastapi import FastAPI
import requests

app = FastAPI(title="API Gateway")

@app.post("/patient-risk-analysis")
def patient_risk_analysis(patient: dict):

    prediction = requests.post(
        "http://localhost:8005/predict",
        json={
            "glucose": patient["glucose"],
            "bmi": patient["bmi"]
        }
    ).json()

    recommendations = requests.post(
        "http://localhost:8006/recommend",
        json=prediction
    ).json()

    requests.post(
        "http://localhost:8007/notify",
        json={
            "patient_id": patient["patient_id"],
            "risk": prediction["risk_level"]
        }
    )

    return {
        "prediction": prediction,
        "recommendations": recommendations
    }
