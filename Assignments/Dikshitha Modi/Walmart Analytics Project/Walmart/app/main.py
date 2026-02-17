from fastapi import FastAPI, Query, HTTPException
import pandas as pd

from app.services.analytics import AnalyticsService
from app.services.anomaly_detection import AnomalyService
from app.services.visualization import VisualizationService
from app.utils.cache import Cache
from app.utils.logger import get_logger


app = FastAPI(title="Walmart Retail Demand & Revenue Intelligence Platform")
logger = get_logger("walmart-app")

# -------------------------------------------------
# Startup: Load CSV ONCE + Precompute everything
# -------------------------------------------------

@app.on_event("startup")
def startup():

    try:
        logger.info("Starting Walmart Analytics Platform...")

        logger.info("Loading Walmart dataset...")
        df = pd.read_csv("app/data/walmart_sales.csv")
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

        logger.info("Performing feature engineering...")
        analytics = AnalyticsService(df)
        analytics.feature_engineering()

        logger.info("Detecting anomalies...")
        anomaly_service = AnomalyService(df)
        anomalies = anomaly_service.zscore()

        app.state.df = Cache.get("df")
        app.state.anomalies = anomalies

        logger.info("Startup completed successfully")

    except Exception as e:
        logger.exception("Startup failed")
        raise e


# -------------------------------------------------
# APIs
# -------------------------------------------------

@app.get("/overview")
async def overview():
    logger.info("GET /overview")
    try:
        return AnalyticsService(app.state.df).overview()
    except Exception as e:
        logger.exception("Overview endpoint failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/store/{store_id}")
async def store_metrics(store_id: int):
    logger.info(f"GET /store/{store_id}")
    try:
        return AnalyticsService(app.state.df).store_metrics(store_id)
    except Exception as e:
        logger.exception("Store metrics failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/anomalies")
async def anomalies(method: str = "zscore", threshold: int = 3):

    logger.info(f"GET /anomalies | method={method} threshold={threshold}")

    try:
        svc = AnomalyService(app.state.df)

        if method == "iqr":
            return svc.iqr().to_dict("records")

        return svc.zscore(threshold).to_dict("records")

    except Exception as e:
        logger.exception("Anomalies endpoint failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/economic-impact")
async def economic_impact():
    logger.info("GET /economic-impact")
    try:
        return AnalyticsService(app.state.df).economic_regression()
    except Exception as e:
        logger.exception("Economic impact failed")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/visualize")
async def visualize(chart: str = Query(...), store: int | None = None):

    logger.info(f"GET /visualize | chart={chart} store={store}")

    try:
        viz = VisualizationService(app.state.df, app.state.anomalies)

        if chart == "trend":
            return viz.weekly_trend(store)

        if chart == "holiday":
            return viz.holiday_boxplot()

        if chart == "economic":
            return viz.economic_scatter()

        if chart == "anomaly":
            return viz.anomaly_plot(store)

        logger.warning("Invalid chart type requested")
        return {"error": "Invalid chart type"}

    except Exception as e:
        logger.exception("Visualization failed")
        raise HTTPException(status_code=500, detail=str(e))
