
import pandas as pd
import pytest
from src.data_collection import load_csv


def test_load_csv_normalizes_columns(tmp_path):
    frame = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02"],
        "Close": [10, 11]
    })

    csv_path = tmp_path / "prices.csv"
    frame.to_csv(csv_path, index=False)

    result = load_csv(str(csv_path))

    assert list(result["close"]) == [10, 11]


def test_load_csv_requires_close(tmp_path):
    frame = pd.DataFrame({
        "Date": ["2024-01-01"]
    })

    csv_path = tmp_path / "invalid.csv"
    frame.to_csv(csv_path, index=False)

    with pytest.raises(ValueError):
        load_csv(str(csv_path))
