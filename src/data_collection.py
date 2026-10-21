"""Historical market data loading utilities."""
from __future__ import annotations
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load historical OHLCV data from a CSV file and validate required columns."""
    frame = pd.read_csv(path)
    frame.columns = [str(c).strip().lower().replace(" ", "_") for c in frame.columns]
    if "date" not in frame.columns:
        raise ValueError("CSV must contain a 'Date' column.")
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"]).sort_values("date").drop_duplicates("date")
    if "close" not in frame.columns:
        raise ValueError("CSV must contain a 'Close' column.")
    frame["close"] = pd.to_numeric(frame["close"], errors="coerce")
    return frame.dropna(subset=["close"]).reset_index(drop=True)

def download_yfinance(ticker: str, period: str = "5y", interval: str = "1d") -> pd.DataFrame:
    """Download market data using yfinance. Network access is required."""
    import yfinance as yf
    data = yf.download(ticker, period=period, interval=interval, auto_adjust=False, progress=False)
    if data.empty:
        raise ValueError(f"No market data returned for ticker {ticker!r}.")
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)
    data = data.reset_index()
    data.columns = [str(c).strip().lower().replace(" ", "_") for c in data.columns]
    if "datetime" in data.columns and "date" not in data.columns:
        data = data.rename(columns={"datetime": "date"})
    if "date" not in data.columns:
        data = data.rename(columns={data.columns[0]: "date"})
    return data
