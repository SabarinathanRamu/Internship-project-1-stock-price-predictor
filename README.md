# Stock Price Predictor

> **Project type:** Four-member group project template  
> **Topic:** Predicting stock prices from historical market data using machine learning.

## Overview

This project explores the assigned topic through a reproducible Python workflow, model comparison, evaluation, and an interactive Streamlit application. The role labels are placeholders; add names to reports only after the team is confirmed.

## Objectives

- Load historical OHLCV data from a CSV file or a supported market-data provider.
- Generate technical features such as moving averages, MACD, RSI, returns, and rolling volatility.
- Compare Linear Regression, Random Forest, and Gradient Boosting using a chronological holdout.
- Report MAE, RMSE, and R² and inspect actual versus predicted next-session closing prices.
- Explore the results in a Streamlit dashboard and export predictions.

## Workflow

1. Load historical market data.
2. Validate dates and closing prices.
3. Generate technical indicators and a next-session target.
4. Train candidate regressors using time-ordered data.
5. Compare holdout metrics and review predictions.
6. Export results for further analysis.

## Data

The app includes **synthetic demo data** so the workflow can be explored without a network connection. Synthetic data is not real market history and must not be used to draw investment conclusions. For meaningful experiments, upload a CSV with at least `Date` and `Close` columns; optional OHLCV columns are supported. The online-download option requires network access and `yfinance`.

## Evaluation and limitations

The evaluation uses a chronological holdout rather than randomly shuffling time-series rows. This is a learning project, not a trading system. Market prices are noisy, data can be revised, and a model's past test performance does not guarantee future performance. Do not use outputs as financial advice.

## Team roles

See [`TEAM_ROLES.md`](TEAM_ROLES.md) for the initial four-role allocation:
- Team Leader
- Member 1
- Member 2
- Member 3

These are role labels, not real names or proof of contribution. Update the allocation to reflect the work actually performed.

## Repository structure

```text
.
├── app.py
├── src/                 # Reusable processing and modelling modules
├── tests/               # Automated tests
├── docs/                # Development plan and meeting template
├── TEAM_ROLES.md
├── requirements.txt
└── README.md
```

## Setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

Run tests:

```bash
python -m pytest
```

## Suggested collaboration workflow

1. Create a GitHub Issue for each task.
2. Work in a feature branch.
3. Open a pull request with a clear summary and test evidence.
4. Request a review from another member.
5. Merge after review and update the progress log.

## Documentation

- [`docs/weekly-progress.md`](docs/weekly-progress.md) — four-week plan and progress log.
- [`docs/meeting-notes-template.md`](docs/meeting-notes-template.md) — template for real meetings.
- [`TEAM_ROLES.md`](TEAM_ROLES.md) — responsibilities.

## License

Choose and add a license after confirming the project's intended use and dataset terms.
