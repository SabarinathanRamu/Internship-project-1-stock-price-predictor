import pandas as pd
from src.features import add_features
from src.sample_data import make_sample_data

def test_feature_generation_has_target():
    featured = add_features(make_sample_data(100))
    assert "target_next_close" in featured.columns
    assert len(featured) > 0
    assert featured["target_next_close"].notna().all()
