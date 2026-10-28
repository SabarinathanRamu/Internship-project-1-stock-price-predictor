
# Stock Price Predictor

> **Project Type:** Five-Member Group Internship Project  
> **Internship:** Artificial Intelligence Internship  
> **Organization:** Codec Technologies  
> **College:** Sindhi College of Arts and Science  
> **Department:** Bachelor of Computer Applications (BCA)  
> **Project Topic:** Stock Price Prediction Using Machine Learning

## Overview

Stock Price Predictor is a Python-based machine learning application developed as part of the Artificial Intelligence Internship at Codec Technologies.

The project explores historical stock market data through a reproducible workflow involving data collection, preprocessing, feature engineering, model training, evaluation, and visualization.

An interactive Streamlit application allows users to explore historical stock prices, compare machine learning models, visualize actual and predicted next-session closing prices, and export results for further analysis.

The project is organized as a five-member group project with responsibilities distributed across leadership, analysis, development, and testing.

## Project Objectives

- Load historical OHLCV stock market data from CSV files or supported market-data providers.
- Generate technical indicators including moving averages, MACD, RSI, returns, and rolling volatility.
- Train and compare Linear Regression, Random Forest, and Gradient Boosting models.
- Use chronological training and testing splits to preserve time-series order.
- Evaluate models using MAE, RMSE, and R².
- Visualize historical stock prices through interactive charts.
- Compare actual and predicted next-session closing prices.
- Export prediction-related results as CSV files.
- Provide an accessible user interface through Streamlit.

## Team Members and Responsibilities

The Stock Price Predictor project is organized as a five-member internship team.

| S. No. | Team Member | Role | Primary Responsibilities |
|---|---|---|---|
| 1 | Sabarinathan R | Leader | Project planning, team coordination, architecture, integration, GitHub management, and final review |
| 2 | Abinaya R | Analyst | Data analysis, dataset inspection, preprocessing analysis, technical indicators, and evaluation interpretation |
| 3 | Sandhiya S | Developer | Python backend development, data collection, feature engineering, and machine learning implementation |
| 4 | Swetha V | Developer | Streamlit frontend development, dashboard design, visualizations, and prediction output integration |
| 5 | Suriyaprakash H | Tester | Unit testing, data validation, debugging, functionality verification, and quality assurance |

For detailed role descriptions, see [TEAM_ROLES.md](TEAM_ROLES.md).

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data processing and manipulation |
| NumPy | Numerical computations |
| Scikit-learn | Machine learning model training and evaluation |
| Plotly | Interactive data visualization |
| yfinance | Historical market-data download |
| Pytest | Automated unit testing |
| Git | Version control |
| GitHub | Repository hosting and collaboration |

## Machine Learning Models

The project compares three regression algorithms:

### 1. Linear Regression

Linear Regression provides a baseline model for predicting the next-session closing price from historical market features.

### 2. Random Forest Regressor

Random Forest combines multiple decision trees to model nonlinear relationships in stock market data.

### 3. Gradient Boosting Regressor

Gradient Boosting builds sequential decision trees to improve prediction performance by learning from previous model errors.

The models are evaluated on chronologically separated training and testing data.

## Project Workflow

1. Collect or load historical stock market data.
2. Validate the input dataset and required columns.
3. Preprocess stock market records.
4. Generate technical indicators and predictive features.
5. Construct the next-session closing-price target.
6. Split the dataset chronologically.
7. Train the machine learning models.
8. Evaluate performance using MAE, RMSE, and R².
9. Visualize historical prices and prediction results.
10. Export results for further analysis.

## Data Sources

The application supports three data-input modes:

### Synthetic Demo Data

Generates sample stock market data for testing and demonstration without requiring an internet connection.

Synthetic data is not actual market history and must not be used to draw investment conclusions.

### Upload Historical CSV

Allows users to upload historical stock market data.

The CSV should include at least:

- Date
- Close

Additional OHLCV fields may be supported depending on the data-loading and validation workflow.

### Download Market Data

Downloads historical stock market data through the yfinance library.

This feature requires an active internet connection and access to the market-data provider.

## Feature Engineering

The application generates technical indicators and derived features, including:

- Daily returns
- Simple Moving Average (SMA 5)
- Simple Moving Average (SMA 20)
- Exponential Moving Average (EMA 12)
- Exponential Moving Average (EMA 26)
- Moving Average Convergence Divergence (MACD)
- Relative Strength Index (RSI 14)
- Rolling volatility
- Next-session closing-price target

These features are used to train and evaluate the regression models.

## Model Evaluation

Model performance is assessed using:

**Mean Absolute Error (MAE)**

Measures the average absolute difference between actual and predicted values.

**Root Mean Squared Error (RMSE)**

Measures prediction error while giving greater weight to larger differences.

**R-squared (R²)**

Measures how well the model explains variation in the target variable.

The project uses a chronological holdout rather than randomly shuffling time-series records.

Historical model performance does not guarantee future prediction accuracy.

## Streamlit Application Features

The interactive dashboard provides:

- Stock market data-source selection
- Stock ticker input
- Historical period selection
- Model training and evaluation
- Historical closing-price visualization
- Model evaluation results
- Actual versus predicted closing-price visualization
- CSV export functionality

The dashboard is intended for educational exploration of machine learning and stock market data.

## Project Repository Structure

```text
Stock-Price-Predictor/
|
|-- app.py
|-- config.py
|-- pyproject.toml
|-- requirements.txt
|-- README.md
|-- TEAM_ROLES.md
|
|-- src/
|   |-- data_collection.py
|   |-- sample_data.py
|   |-- features.py
|   |-- modeling.py
|
|-- tests/
|   |-- test_data_collection.py
|   |-- test_data_validation.py
|   |-- test_evaluation.py
|   |-- test_features.py
|
|-- data/
|-- docs/
```

This structure summarizes the main project components.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SabarinathanRamu/Internship-project-1-stock-price-predictor.git
```

### Step 2: Open the Project Directory

```bash
cd Internship-project-1-stock-price-predictor
```

### Step 3: Create a Virtual Environment

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

Windows:

```bat
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Launch the Streamlit Application

```bash
python -m streamlit run app.py
```

Open the local application address displayed in the terminal.

The default Streamlit address is:

http://localhost:8501

## Running Automated Tests

The project uses Pytest for unit testing.

Run:

```bash
python -m pytest -v
```

The test suite covers areas including:

- Data collection
- Data validation
- Feature engineering
- Chronological splitting
- Model evaluation functionality

### Recorded Local Test Result

During local project verification, the test execution produced:

```text
7 passed in 5.74s
```

This is a recorded local result, not a guarantee that every future checkout or modification will produce the same outcome.

Run the tests again after changing project files.

## Team Collaboration Workflow

The five-member team follows a collaborative project workflow.

1. Define project requirements and assign responsibilities.
2. Analyze historical stock market data.
3. Develop backend data processing and machine learning modules.
4. Develop and integrate the Streamlit dashboard.
5. Execute tests and resolve identified issues.
6. Review the integrated application.
7. Prepare technical documentation and the internship report.
8. Maintain the project through Git and GitHub.

All team members may participate in reviews, integration, testing, and documentation.

## Documentation

Additional project documentation is available in:

- [TEAM_ROLES.md](TEAM_ROLES.md) — Team members and assigned responsibilities.
- [docs/weekly-progress.md](docs/weekly-progress.md) — Development plan and progress documentation.
- [docs/meeting-notes-template.md](docs/meeting-notes-template.md) — Team meeting documentation template.

## Project Limitations

- Stock market prices are affected by unpredictable economic and market conditions.
- Historical patterns may not remain consistent in future trading sessions.
- Machine learning predictions may contain significant errors.
- Synthetic demonstration data does not represent actual market conditions.
- Online market-data downloads depend on external services.
- Model evaluation results depend on the dataset and evaluation period.

The application is designed for academic learning and experimentation, not live trading or investment decision-making.

## Future Enhancements

Potential improvements include:

- Additional machine learning algorithms
- Improved time-series evaluation techniques
- Expanded technical indicators
- Hyperparameter optimization
- Enhanced dashboard visualizations
- Additional market-data sources
- Automated model performance reports
- Improved prediction export formats
- Deployment to a cloud hosting platform

## Project Repository

**GitHub:**

https://github.com/SabarinathanRamu/Internship-project-1-stock-price-predictor

**Project:** Stock Price Predictor

**Internship Organization:** Codec Technologies

**Department:** BCA

**Team Size:** Five Members

## Conclusion

The Stock Price Predictor project demonstrates the application of Python, data processing, technical feature engineering, and machine learning to historical stock market data.

The project integrates data collection, model training, evaluation, interactive visualization, and automated testing into a single educational application.

Through this five-member group project, the team develops practical experience in software development, machine learning workflows, data analysis, application testing, version control, and technical documentation.

## License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2026 Stock Price Predictor Project Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
