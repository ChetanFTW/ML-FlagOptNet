import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_model(csv_path="dataset.csv"):
    df = pd.read_csv(csv_path)
    X = pd.get_dummies(df.drop(columns=["runtime_ms", "file"]))
    y = df["runtime_ms"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"✅ Model R² score: {score:.3f}")

if __name__ == "__main__":
    train_model()
