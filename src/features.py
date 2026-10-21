"""Leakage-aware technical feature generation."""
from __future__ import annotations
import pandas as pd

def add_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Add rolling indicators; target is next session's close."""
    df = frame.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    if "close" not in df:
        raise ValueError("Input data must include a close column.")
    close = pd.to_numeric(df["close"], errors="coerce")
    df["return_1d"] = close.pct_change()
    df["sma_5"] = close.rolling(5).mean()
    df["sma_20"] = close.rolling(20).mean()
    df["ema_12"] = close.ewm(span=12, adjust=False).mean()
    df["ema_26"] = close.ewm(span=26, adjust=False).mean()
    df["macd"] = df["ema_12"] - df["ema_26"]
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / loss.replace(0, float("nan"))
    df["rsi_14"] = 100 - (100 / (1 + rs))
    df["volatility_20"] = df["return_1d"].rolling(20).std()
    df["target_next_close"] = close.shift(-1)
    return df.replace([float("inf"), float("-inf")], float("nan")).dropna().reset_index(drop=True)
