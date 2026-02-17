# Analytics service module
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from app.utils.cache import Cache


class AnalyticsService:

    def __init__(self, df):
        self.df = df

    def feature_engineering(self):

        self.df["sales_volatility"] = self.df.groupby("Store")["Weekly_Sales"].transform(
            lambda x: x / x.mean()
        )

        holiday = self.df[self.df["Holiday_Flag"] == 1].groupby("Store")["Weekly_Sales"].mean()
        non = self.df[self.df["Holiday_Flag"] == 0].groupby("Store")["Weekly_Sales"].mean()

        self.df["holiday_impact"] = self.df["Store"].map(holiday - non)

        self.df["stress_index"] = (
            self.df["Fuel_Price"] * 0.4 +
            self.df["CPI"] * 0.3 +
            self.df["Unemployment"] * 0.3
        )

        Cache.set("df", self.df)

    def overview(self):

        df = Cache.get("df")

        return {
            "total_stores": df["Store"].nunique(),
            "total_weeks": df["Date"].nunique(),
            "avg_weekly_sales": round(df["Weekly_Sales"].mean(), 2),
            "holiday_sales_lift_percent":
                round((df[df.Holiday_Flag==1].Weekly_Sales.mean() /
                df[df.Holiday_Flag==0].Weekly_Sales.mean() -1)*100,2)
        }

    def store_metrics(self, store):

        df = Cache.get("df")
        s = df[df.Store == store]

        if s.empty:
            return {
                "error": "Store not found"
            }

        corr = s["stress_index"].corr(s["Weekly_Sales"])

        return {
            "avg_sales": float(s.Weekly_Sales.mean()),
            "volatility": float(s.sales_volatility.std()),
            "holiday_impact": float(s.holiday_impact.mean()),
            "stress_sales_corr": float(corr)
        }


    def economic_regression(self):

        df = Cache.get("df")

        X = df[["Fuel_Price","CPI","Unemployment"]]
        y = df["Weekly_Sales"]

        model = LinearRegression().fit(X,y)

        return {
            "coefficients": dict(zip(X.columns, model.coef_)),
            "importance_rank":
                sorted(zip(X.columns, abs(model.coef_)), key=lambda x:x[1], reverse=True)
        }
