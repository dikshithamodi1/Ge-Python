# Walmart Retail Demand & Revenue Intelligence Platform

## Project Overview

This project simulates a real-world analytics engineering assignment at Walmart Global Tech, where the Data Engineering and Backend Analytics team is responsible for building a scalable analytics microservice that transforms retail sales data into actionable business intelligence. The platform provides store-level performance insights, detects anomalies, evaluates economic impact, and exposes analytics through FastAPI endpoints with dynamic visualization support.

The system is implemented as a production-style FastAPI backend using NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, structured logging, and automated testing.

## Business Context

Retail leadership requires a data-backed decision system to understand store performance, holiday impact, sales volatility, economic influence, and predictive indicators for inventory planning. This platform answers the following questions:

Which stores are high-performing or volatile  
How holidays affect weekly revenue  
How fuel price, CPI, and unemployment influence sales  
Which weeks exhibit anomalous behavior  
How economic stress correlates with demand  
How stores can be classified based on stability  

## Dataset

Source: Kaggle Walmart Sales Dataset  
https://www.kaggle.com/datasets/mikhail1681/walmart-sales/data

Columns

Store – Store number  
Date – Weekly sales date  
Weekly_Sales – Weekly sales amount  
Sales – Aggregated sales  
Holiday_Flag – 1 = Holiday week, 0 = Non-holiday  
Temperature – Air temperature in Fahrenheit  
Fuel_Price – Regional fuel price  
CPI – Consumer Price Index  
Unemployment – Unemployment rate  

## Part 1 Data Engineering and Analytics

Feature Engineering is fully vectorized using NumPy and Pandas without loops.

Sales Volatility is calculated as Weekly_Sales divided by the mean Weekly_Sales per store. This measures how much each week deviates from a store’s typical performance.

Holiday Impact Score is computed as the average holiday sales minus average non-holiday sales for each store, quantifying seasonal uplift.

Economic Stress Index is calculated using NumPy broadcasting:

stress_index = Fuel_Price * 0.4 + CPI * 0.3 + Unemployment * 0.3

Store and Time-Based Analysis includes monthly average sales per store, top five stores by mean weekly sales and lowest volatility, holiday versus non-holiday percentage change, and seasonality identification using four-week rolling averages.

Advanced Analytics includes Z-score anomaly detection, IQR-based anomaly detection, correlation analysis between Fuel Price, CPI, Unemployment and Weekly Sales, and store classification into Stable, Seasonal, or Highly Volatile categories based on standard deviation thresholds.

## Part 2 FastAPI Analytics Service

The backend follows enterprise constraints: CSV is loaded once at startup, heavy computations are cached, APIs are asynchronous, and no recomputation occurs per request. Lifespan-based initialization is used and structured logging captures startup, API access, and errors. Fifteen automated unit tests validate functionality.

Available endpoints:

GET /overview returns total stores, total weeks, average weekly sales, and holiday sales lift percentage.

GET /store/{store_id} returns average weekly sales, volatility score, holiday impact, and economic stress versus sales correlation. Invalid stores are handled safely.

GET /anomalies supports Z-score and IQR detection through query parameters and returns Store, Date, Weekly_Sales, and reason flagged.

GET /compare-stores compares two stores by mean sales, standard deviation, and holiday performance delta.

GET /economic-impact performs linear regression and returns coefficients, feature importance ranking, and interpretation-ready results.

## Part 3 Visualization

Dynamic visualizations are generated via the /visualize endpoint.

Supported charts:

Weekly Sales Trend per Store with rolling average  
Holiday versus Non-Holiday Sales box plot  
Economic scatter plots for Fuel Price, CPI, and Unemployment versus Sales  
Anomaly visualization with highlighted outliers on time series  

Matplotlib runs in non-GUI mode to support automated testing environments.

## Project Architecture

```
Walmart/
│
├── app/
│   │
│   ├── main.py                     # FastAPI entry point, lifespan startup, API routes
│   │
│   ├── data/
│   │   └── walmart_sales.csv       # Raw Kaggle dataset (loaded once at startup)
│   │
│   ├── services/
│   │   ├── analytics.py            # Feature engineering, store analytics, regression
│   │   ├── anomaly_detection.py    # Z-score & IQR anomaly detection logic
│   │   └── visualization.py        # Matplotlib/Seaborn chart generation
│   │
│   ├── models/
│   │   └── response_models.py      # Pydantic response schemas (optional extension)
│   │
│   ├── utils/
│   │   ├── cache.py                # In-memory caching for heavy computations
│   │   └── logger.py               # Structured logging (console + file)
│   │
│   └── __init__.py
│
├── logs/
│   └── walmart.logs                # Application runtime logs
│
├── tests/
│   └── test_api.py                # 15 automated Pytest API test cases
│
├── README.md                      # Detailed project documentation

```

The services layer handles analytics, anomaly detection, and visualization. Utilities provide caching and logging. Tests validate API behavior.

## Logging

Structured logging is implemented with both console and file handlers. Logs are stored in logs/walmart.logs and include startup events, API requests, error traces, and shutdown messages.

## Testing

Fifteen automated Pytest test cases validate all endpoints, anomaly detection, regression output, visualization routes, and edge cases. Lifecycle-aware TestClient ensures startup execution during tests.

Run tests using:

python -m pytest -v

## Running the Application

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn app.main:app --reload

Access Swagger documentation at:

http://127.0.0.1:8000/docs

