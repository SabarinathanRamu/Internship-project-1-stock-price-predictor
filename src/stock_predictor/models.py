from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression

def build_model(name: str, random_state: int = 42):
    if name == "Linear Regression":
        return LinearRegression()
    if name == "Gradient Boosting":
        return GradientBoostingRegressor(
            n_estimators=180, learning_rate=0.04, max_depth=2, random_state=random_state
        )
    if name == "Random Forest":
        return RandomForestRegressor(
            n_estimators=250, min_samples_leaf=2, random_state=random_state, n_jobs=-1
        )
    raise ValueError(f"Unknown model: {name}")
