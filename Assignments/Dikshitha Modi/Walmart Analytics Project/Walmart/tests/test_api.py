from fastapi.testclient import TestClient
from app.main import app

def get_client():
    return TestClient(app)


# ---------------------------------------------------
# BASIC PLATFORM TESTS
# ---------------------------------------------------

def test_overview_status():
    with get_client() as client:
        res = client.get("/overview")
        assert res.status_code == 200


def test_overview_keys():
    with get_client() as client:
        data = client.get("/overview").json()
        assert "total_stores" in data
        assert "avg_weekly_sales" in data


def test_overview_values():
    with get_client() as client:
        data = client.get("/overview").json()
        assert data["total_stores"] > 0
        assert data["avg_weekly_sales"] > 0


# ---------------------------------------------------
# STORE ENDPOINT
# ---------------------------------------------------

def test_store_valid():
    with get_client() as client:
        res = client.get("/store/1")
        assert res.status_code == 200


def test_store_fields():
    with get_client() as client:
        data = client.get("/store/1").json()
        assert "avg_sales" in data
        assert "volatility" in data
        assert "holiday_impact" in data


def test_store_invalid():
    with get_client() as client:
        res = client.get("/store/999")
        assert "error" in res.json()



# ---------------------------------------------------
# ANOMALIES
# ---------------------------------------------------

def test_anomalies_default():
    with get_client() as client:
        res = client.get("/anomalies")
        assert res.status_code == 200
        assert isinstance(res.json(), list)


def test_anomalies_zscore():
    with get_client() as client:
        res = client.get("/anomalies?method=zscore")
        assert res.status_code == 200


def test_anomalies_iqr():
    with get_client() as client:
        res = client.get("/anomalies?method=iqr")
        assert res.status_code == 200


def test_anomaly_fields():
    with get_client() as client:
        data = client.get("/anomalies").json()
        if len(data) > 0:
            row = data[0]
            assert "Store" in row
            assert "Weekly_Sales" in row
            assert "reason" in row


# ---------------------------------------------------
# ECONOMIC IMPACT
# ---------------------------------------------------

def test_economic_status():
    with get_client() as client:
        res = client.get("/economic-impact")
        assert res.status_code == 200


def test_economic_keys():
    with get_client() as client:
        data = client.get("/economic-impact").json()
        assert "coefficients" in data
        assert "importance_rank" in data


# ---------------------------------------------------
# VISUALIZATION
# ---------------------------------------------------

def test_visualize_holiday():
    with get_client() as client:
        res = client.get("/visualize?chart=holiday")
        assert res.status_code == 200


def test_visualize_trend():
    with get_client() as client:
        res = client.get("/visualize?chart=trend&store=1")
        assert res.status_code == 200


def test_visualize_invalid_chart():
    with get_client() as client:
        res = client.get("/visualize?chart=xyz")
        assert res.status_code == 200
        assert "error" in res.json()
