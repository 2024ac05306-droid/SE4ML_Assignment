# evaluate_model.py
import joblib
from sklearn.metrics import accuracy_score, classification_report

# Paths should match those used in train_model.py
MODEL_PATH = "models/diabetes_model.pkl"
TEST_DATA_PATH = "models/test_data.pkl"

def evaluate(model_path=MODEL_PATH, test_data_path=TEST_DATA_PATH):
    # Load model
    model = joblib.load(model_path)

    # Load test split saved by train_model.py
    X_test, y_test = joblib.load(test_data_path)

    # Predict and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    evaluate()
