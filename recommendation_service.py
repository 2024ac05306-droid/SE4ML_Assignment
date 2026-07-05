# recommendation_service.py

from fastapi import FastAPI

app = FastAPI(title="Recommendation Service")

@app.post("/recommend")
def recommend(data: dict):

    if data["risk_level"] == "HIGH":

        recommendation = [
            "Consult Doctor",
            "Reduce Sugar Intake",
            "Daily Exercise"
        ]

    else:

        recommendation = [
            "Maintain Healthy Lifestyle"
        ]

    return {"recommendations": recommendation}
