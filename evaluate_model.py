# evaluate_model.py
from data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = load_data()

# Prepare features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Create train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Load trained model
model = joblib.load("models/diabetes_model.pkl")

# Predict
predictions = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")
