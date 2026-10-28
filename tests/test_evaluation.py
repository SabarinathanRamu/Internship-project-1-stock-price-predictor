import pytest
import pandas as pd
from stock_predictor.features import add_features
from stock_predictor.evaluation import chronological_split

def test_chronological_split_keeps_order():
    idx = pd.date_range("2020-01-01", periods=500, freq="B")
    close = pd.Series(
    [100 + i * 0.1 + (i % 7) * 2 for i in range(500)],
    index=idx,
    dtype=float
    )
    prices = pd.DataFrame({"Open": close, "High": close+1, "Low": close-1, "Close": close, "Volume": 1000}, index=idx)
    train, test = chronological_split(add_features(prices), 0.2)
    assert train.index.max() < test.index.min()

def test_invalid_test_fraction():
    with pytest.raises(ValueError):
        chronological_split(pd.DataFrame(), 0.05)
