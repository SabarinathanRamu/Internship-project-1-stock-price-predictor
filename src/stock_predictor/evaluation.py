from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from .features import FEATURE_COLUMNS, model_rows
from .models import build_model

def chronological_split(frame: pd.DataFrame, test_fraction: float = 0.2):
    if not 0.1 <= test_fraction <= 0.4:
        raise ValueError("test_fraction must be between 0.1 and 0.4.")
    clean = model_rows(frame)
    split = int(len(clean) * (1 - test_fraction))
    train, test = clean.iloc[:split], clean.iloc[split:]
    if len(train) < 30 or len(test) < 5:
        raise ValueError("Not enough rows after feature engineering. Use a longer date range.")
    return train, test

def evaluate_model(train: pd.DataFrame, test: pd.DataFrame, model_name: str):
    model = build_model(model_name)
    model.fit(train[FEATURE_COLUMNS], train["Target_Next_Close"])
    predictions = model.predict(test[FEATURE_COLUMNS])
    actual = test["Target_Next_Close"].to_numpy()
    previous = test["Close"].to_numpy()
    metrics = {
        "MAE": float(mean_absolute_error(actual, predictions)),
        "RMSE": float(np.sqrt(mean_squared_error(actual, predictions))),
        "R2": float(r2_score(actual, predictions)) if len(actual) > 1 else float("nan"),
        "Directional accuracy": float(np.mean(np.sign(predictions - previous) == np.sign(actual - previous))),
    }
    output = pd.DataFrame({"Actual": actual, "Predicted": predictions, "Previous close": previous}, index=test.index)
    return model, metrics, output

def baseline_metrics(test: pd.DataFrame):
    actual = test["Target_Next_Close"].to_numpy()
    baseline = test["Close"].to_numpy()
    return {
        "Baseline": "Previous close",
        "MAE": float(mean_absolute_error(actual, baseline)),
        "RMSE": float(np.sqrt(mean_squared_error(actual, baseline))),
    }
