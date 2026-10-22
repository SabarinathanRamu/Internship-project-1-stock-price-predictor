
"""Deterministic synthetic OHLCV data for demos and tests only."""
import numpy as np
import pandas as pd


def make_sample_data(
    rows: int | None = None,
    seed: int = 7,
    period: str = "5y",
) -> pd.DataFrame:
    """Generate synthetic business-day stock data for the selected period."""
    period_years = {
        "1y": 1,
        "2y": 2,
        "5y": 5,
        "10y": 10,
    }

    if period not in period_years:
        raise ValueError(
            f"Unsupported period: {period}. Choose from {list(period_years)}"
        )

    if rows is None:
        rows = 252 * period_years[period]

    rng = np.random.default_rng(seed)

    # End on today's date and generate the requested number of business days.
    dates = pd.bdate_range(
        end=pd.Timestamp.today().normalize(),
        periods=rows,
    )

    returns = rng.normal(0.0004, 0.015, rows)
    close = 100 * np.cumprod(1 + returns)
    open_ = close * (1 + rng.normal(0, 0.003, rows))
    high = np.maximum(open_, close) * (1 + rng.uniform(0, 0.01, rows))
    low = np.minimum(open_, close) * (1 - rng.uniform(0, 0.01, rows))
    volume = rng.integers(100_000, 2_000_000, rows)

    return pd.DataFrame({
        "date": dates,
        "open": open_,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume,
    })
