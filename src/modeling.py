"""Chronological model training and evaluation."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FEATURES = ["close", "return_1d", "sma_5", "sma_20", "ema_12", "ema_26", "macd", "rsi_14", "volatility_20"]
@dataclass
class ModelResult:
    name: str
    model: object
    mae: float
    rmse: float
    r2: float

def train_models(featured: pd.DataFrame, test_fraction: float = 0.2) -> tuple[list[ModelResult], pd.DataFrame]:
    """Train/evaluate models using a chronological split (no random shuffling)."""
    missing = [c for c in FEATURES + ["target_next_close"] if c not in featured]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    data = featured.dropna(subset=FEATURES + ["target_next_close"]).reset_index(drop=True)
    if len(data) < 30:
        raise ValueError("At least 30 usable rows are recommended for a chronological evaluation.")
    split = int(len(data) * (1 - test_fraction))
    split = min(max(split, 1), len(data) - 1)
    x_train, x_test = data.loc[:split-1, FEATURES], data.loc[split:, FEATURES]
    y_train, y_test = data.loc[:split-1, "target_next_close"], data.loc[split:, "target_next_close"]
    models = {
        "Linear Regression": make_pipeline(StandardScaler(), LinearRegression()),
        "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42, min_samples_leaf=2),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    }
    results = []
    for name, model in models.items():
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        rmse = float(np.sqrt(mean_squared_error(y_test, pred)))
        results.append(ModelResult(name, model, float(mean_absolute_error(y_test, pred)), rmse, float(r2_score(y_test, pred))))
    return results, data.iloc[split:].assign(actual=y_test.to_numpy())
