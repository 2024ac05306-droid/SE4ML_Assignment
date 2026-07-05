# ml_prediction_service.py

import joblib

model = joblib.load("models/diabetes_model.pkl")
prediction = model.predict([features])
