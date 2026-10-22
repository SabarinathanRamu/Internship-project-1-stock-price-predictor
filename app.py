"""Streamlit dashboard for the Stock Price Predictor."""
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_collection import load_csv, download_yfinance
from src.features import add_features
from src.modeling import train_models
from src.sample_data import make_sample_data

st.set_page_config(page_title="Stock Price Predictor", page_icon="📈", layout="wide")
st.title("Stock Price Predictor")
st.caption("Machine-learning experiments on historical market data. Educational use only; not financial advice.")
with st.sidebar:
    st.header("Data source")
    mode = st.radio("Choose input", ["Synthetic demo data", "Upload historical CSV", "Download market data"])
    ticker = st.text_input("Ticker symbol", "AAPL").strip().upper()
    uploaded = st.file_uploader("Upload CSV (Date and Close required)", type=["csv"]) if mode == "Upload historical CSV" else None
    period = st.selectbox("Download period", ["1y", "2y", "5y", "10y"], index=2)
    run = st.button("Train and evaluate models", type="primary")
if "results" not in st.session_state:
    st.session_state.results = None
if run:
    try:
        if mode == "Synthetic demo data":
            raw = make_sample_data(period=period)
        elif mode == "Upload historical CSV":
            if uploaded is None:
                st.error("Upload a CSV file first.")
                st.stop()
            raw = load_csv(uploaded)
        else:
            raw = download_yfinance(ticker, period=period)
        featured = add_features(raw)
        results, predictions = train_models(featured)
        st.session_state.results = (raw, featured, results, predictions, ticker, mode)
    except Exception as exc:
        st.error(f"Could not run the pipeline: {exc}")
if st.session_state.results:
    raw, featured, results, predictions, ticker, mode = st.session_state.results
    st.subheader("Historical closing price")
    if "date" in raw.columns:
        st.plotly_chart(px.line(raw, x="date", y="close", title="Historical Close"), use_container_width=True)
    cols = st.columns(len(results))
    for col, result in zip(cols, results):
        col.metric(result.name, f"RMSE {result.rmse:.3f}", f"MAE {result.mae:.3f}")
    st.subheader("Actual vs predicted next-session close")
    chart = predictions[["actual"]].copy()
    chart["predicted"] = results[0].model.predict(predictions[__import__("src.modeling", fromlist=["FEATURES"]).FEATURES])
    st.plotly_chart(px.line(chart, y=["actual", "predicted"]), use_container_width=True)
    st.caption("Evaluation uses a chronological holdout. Past performance does not establish future performance.")
    st.download_button("Download predictions CSV", predictions.to_csv(index=False).encode(), "stock_predictions.csv", "text/csv")
else:
    st.info("Choose a data source, then select **Train and evaluate models**.")
    st.write("Synthetic data is provided for demonstration; use real historical data for meaningful evaluation.")
