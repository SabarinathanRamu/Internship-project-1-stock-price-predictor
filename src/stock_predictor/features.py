from __future__ import annotations
import numpy as np
import pandas as pd

FEATURE_COLUMNS = [
    "Open", "High", "Low", "Close", "Volume", "Daily_Return",
    "SMA_10", "SMA_20", "SMA_50", "EMA_12", "EMA_26",
    "MACD", "MACD_Signal", "RSI_14", "Volatility_20"
]

def add_features(prices: pd.DataFrame) -> pd.DataFrame:
    """Create backward-looking indicators and next-session target."""
    data = prices.copy()
    close = data["Close"].astype(float)
    data["Daily_Return"] = close.pct_change() * 100
    for window in (10, 20, 50):
        data[f"SMA_{window}"] = close.rolling(window).mean()
    data["EMA_12"] = close.ewm(span=12, adjust=False).mean()
    data["EMA_26"] = close.ewm(span=26, adjust=False).mean()
    data["MACD"] = data["EMA_12"] - data["EMA_26"]
    data["MACD_Signal"] = data["MACD"].ewm(span=9, adjust=False).mean()
    change = close.diff()
    gains = change.clip(lower=0).rolling(14).mean()
    losses = -change.clip(upper=0).rolling(14).mean()
    rs = gains / losses.replace(0, np.nan)
    data["RSI_14"] = 100 - (100 / (1 + rs))
    data["Volatility_20"] = data["Daily_Return"].rolling(20).std()
    data["Target_Next_Close"] = close.shift(-1)
    return data.replace([np.inf, -np.inf], np.nan)

def model_rows(features: pd.DataFrame) -> pd.DataFrame:
    return features.dropna(subset=FEATURE_COLUMNS + ["Target_Next_Close"]).copy()
