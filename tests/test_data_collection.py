import pandas as pd
import pytest
from src.data_collection import load_csv

def test_load_csv_normalizes_columns():
    frame = load_csv(pd.DataFrame({"Date": ["2024-01-01", "2024-01-02"], "Close": [10, 11]}))
    assert list(frame["close"]) == [10, 11]

def test_load_csv_requires_close():
    with pytest.raises(ValueError):
        load_csv(pd.DataFrame({"Date": ["2024-01-01"]}))
