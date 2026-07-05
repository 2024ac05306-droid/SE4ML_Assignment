# evaluate_model.py

from sklearn.metrics import accuracy_score
import joblib

model = joblib.load("models/diabetes_model.pkl")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
