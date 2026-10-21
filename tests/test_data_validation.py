import pandas as pd
import pytest
from stock_predictor.data import validate_ohlcv

def test_missing_columns_raises():
    with pytest.raises(ValueError):
        validate_ohlcv(pd.DataFrame({"Close": [10]}))

def test_valid_data_is_sorted_and_cleaned():
    idx = pd.to_datetime(["2024-01-02", "2024-01-01"])
    frame = pd.DataFrame({"Open":[11,10],"High":[12,11],"Low":[9,8],"Close":[10,9],"Volume":[100,200]}, index=idx)
    out = validate_ohlcv(frame)
    assert out.index.is_monotonic_increasing
