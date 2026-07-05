# user_service.py

from fastapi import FastAPI

app = FastAPI(title="User Service")

users = []

@app.post("/register")
def register_user(user: dict):
    users.append(user)
    return {"message": "User registered successfully"}

@app.get("/users")
def get_users():
    return users
