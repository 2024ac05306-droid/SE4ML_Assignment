# train_model.py

from data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


def train_and_save(model_path="models/diabetes_model.pkl", test_data_path="models/test_data.pkl"):
    """Load data using data_loader.load_data(), train a RandomForest model,
    and save both the model and test split to the models/ directory.
    """
    df = load_data()

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, model_path)
    # Save the test split so evaluate_model.py can reuse it
    joblib.dump((X_test, y_test), test_data_path)

    print(f"Model trained and saved to {model_path}")
    print(f"Test data saved to {test_data_path}")


if __name__ == "__main__":
    train_and_save()
