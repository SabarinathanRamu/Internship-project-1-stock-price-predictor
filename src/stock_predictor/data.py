from __future__ import annotations
import pandas as pd
import yfinance as yf

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]

def validate_ohlcv(frame: pd.DataFrame) -> pd.DataFrame:
    """Validate, normalize, sort, and clean an OHLCV data frame."""
    if frame is None or frame.empty:
        raise ValueError("No market data was returned. Check the ticker and date range.")
    data = frame.copy()
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    data = data[REQUIRED_COLUMNS].copy()
    for column in REQUIRED_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data = data.dropna(subset=["Open", "High", "Low", "Close"])
    data = data[~data.index.duplicated(keep="last")].sort_index()
    if data.empty:
        raise ValueError("No valid price rows remain after cleaning.")
    if (data[["Open", "High", "Low", "Close"]] <= 0).any().any():
        data = data[(data[["Open", "High", "Low", "Close"]] > 0).all(axis=1)]
    if data.empty:
        raise ValueError("Price data contains no positive price rows.")
    data["Volume"] = data["Volume"].fillna(0).clip(lower=0)
    return data

def download_history(ticker: str, start, end) -> pd.DataFrame:
    """Download adjusted daily OHLCV history. End date is inclusive in the UI."""
    ticker = ticker.strip().upper()
    if not ticker:
        raise ValueError("Please enter a stock ticker.")
    inclusive_end = pd.Timestamp(end) + pd.Timedelta(days=1)
    raw = yf.download(
        ticker, start=str(start), end=inclusive_end.strftime("%Y-%m-%d"),
        auto_adjust=True, progress=False, threads=False
    )
    return validate_ohlcv(raw)
