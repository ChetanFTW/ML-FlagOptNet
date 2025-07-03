import xgboost as xgb
import pandas as pd
import re
from pathlib import Path
from extract_features import get_ast, extract_features

def predict_runtime(cfile_path: str, model_data="dataset.csv"):
    print(f"[🚀] Testing: {cfile_path}")
    ast = get_ast(Path(cfile_path))
    if not ast.strip():
        print("[⚠️] Empty AST. Clang may have failed.")
        return

    feats = extract_features(ast)
    if not feats:
        print("[⚠️] Feature extraction failed.")
        return

    feats["loc"] = sum(1 for _ in open(cfile_path))
    feats["flags"] = "-O2"  # Use same as in training

    # Load training data to get feature layout
    df = pd.read_csv(model_data)
    X_train = pd.get_dummies(df.drop(columns=["runtime_ms", "file"]))
    feature_order = X_train.columns

    # Build test row
    test_df = pd.DataFrame([feats])
    test_df = pd.get_dummies(test_df)
    test_df = test_df.reindex(columns=feature_order, fill_value=0)

    model = xgb.XGBRegressor()
    model.fit(X_train, df["runtime_ms"])  # You can also load from saved model

    predicted = model.predict(test_df)[0]
    print(f"🔮 Predicted runtime (ms): {predicted:.2f}")

if __name__ == "__main__":
    predict_runtime("c_sources/test_case.c")
