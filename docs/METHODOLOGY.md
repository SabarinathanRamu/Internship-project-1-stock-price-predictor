# Methodology — Stock Price Predictor

## Prediction target
For each session, the target is the following session's closing price. The final row has no target because the next session is not present in the downloaded history.

## Features
All indicators are computed from current and prior observations: returns, moving averages, exponential moving averages, MACD, RSI, and rolling volatility. When extending this project, ensure each feature would be available at the prediction time.

## Evaluation design
Rows are sorted by date and split chronologically. The earlier segment is used for fitting; the later segment is held out for evaluation. The previous-close baseline is included because a complex model should be compared to a simple reference.

## Metrics
MAE and RMSE are expressed in price units. R² can be negative when predictions are worse than a constant-mean reference. Directional accuracy compares the sign of predicted versus observed change from the previous close.

## Caveats
The interface is a research and learning tool. A single hold-out window is not enough to establish robust performance. Further work should use rolling-origin evaluation, account for transaction costs where relevant, and report uncertainty honestly.
