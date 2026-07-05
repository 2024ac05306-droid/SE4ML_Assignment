# notification_service.py

from fastapi import FastAPI

app = FastAPI(title="Notification Service")

@app.post("/notify")
def notify(data: dict):

    print("Sending Notification:", data)

    return {
        "message": "Notification sent"
    }
