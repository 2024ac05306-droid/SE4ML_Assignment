# ml_prediction_service.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

MODEL_PATH = "models/diabetes_model.pkl"

app = Flask(__name__)

# Load model once at startup
model = joblib.load(MODEL_PATH)

# Expected feature order:
FEATURES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts JSON with either:
    - a single record: {"features": [val1, val2, ...]}
    - or a dict of named features: {"Pregnancies":..., "Glucose":..., ...}
    - or multiple records: {"instances": [[...], [...]]}
    Returns predicted class and probability if available.
    """
    data = request.get_json(force=True)

    # support multiple input formats
    if not data:
        return jsonify({"error": "Empty request body"}), 400

    if "instances" in data:
        df = pd.DataFrame(data["instances"], columns=FEATURES)
    elif "features" in data:
        df = pd.DataFrame([data["features"]], columns=FEATURES)
    else:
        # assume a mapping of feature names
        df = pd.DataFrame([data], columns=FEATURES)

    try:
        preds = model.predict(df).tolist()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df).tolist()

    response = {"predictions": preds}
    if proba is not None:
        response["probabilities"] = proba

    return jsonify(response), 200

if __name__ == "__main__":
    # For development only; use a WSGI server for production
    app.run(host="0.0.0.0", port=5000)
