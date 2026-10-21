from __future__ import annotations
import pandas as pd

def safe_csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=True).encode("utf-8")
