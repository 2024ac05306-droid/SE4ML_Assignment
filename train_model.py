# train_model.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data_loader import load_data
import joblib
import os

# Load dataset 
df = load_data()

# Features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/diabetes_model.pkl")

print("Model trained and saved successfully.")
