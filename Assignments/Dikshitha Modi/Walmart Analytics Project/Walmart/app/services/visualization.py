# Visualization service module
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
from fastapi.responses import StreamingResponse

sns.set(style="whitegrid")


class VisualizationService:

    def __init__(self, df: pd.DataFrame, anomalies: pd.DataFrame):
        self.df = df
        self.anomalies = anomalies

        # Ensure datetime
        self.df["Date"] = pd.to_datetime(self.df["Date"])

    # --------------------------------------------------
    # 1️⃣ Weekly Sales Trend + Rolling Average
    # --------------------------------------------------
    def weekly_trend(self, store_id: int):

        data = self.df[self.df["Store"] == store_id].sort_values("Date")
        data["rolling"] = data["Weekly_Sales"].rolling(4).mean()

        plt.figure(figsize=(12, 6))
        plt.plot(data["Date"], data["Weekly_Sales"], label="Weekly Sales")
        plt.plot(data["Date"], data["rolling"], label="4W Rolling Avg")

        plt.title(f"Weekly Sales Trend – Store {store_id}")
        plt.legend()

        return self._export_plot()

    # --------------------------------------------------
    # 2️⃣ Holiday vs Non-Holiday Boxplot
    # --------------------------------------------------
    def holiday_boxplot(self):

        plt.figure(figsize=(7, 5))
        sns.boxplot(
            x="Holiday_Flag",
            y="Weekly_Sales",
            data=self.df
        )

        plt.title("Holiday vs Non-Holiday Sales")
        plt.xlabel("Holiday Flag (1=Holiday)")
        plt.ylabel("Weekly Sales")

        return self._export_plot()

    # --------------------------------------------------
    # 3️⃣ Economic Factors Scatter
    # --------------------------------------------------
    def economic_scatter(self):

        fig, axes = plt.subplots(1, 3, figsize=(15, 4))

        sns.scatterplot(ax=axes[0], x="Fuel_Price", y="Weekly_Sales", data=self.df)
        sns.scatterplot(ax=axes[1], x="CPI", y="Weekly_Sales", data=self.df)
        sns.scatterplot(ax=axes[2], x="Unemployment", y="Weekly_Sales", data=self.df)

        axes[0].set_title("Fuel vs Sales")
        axes[1].set_title("CPI vs Sales")
        axes[2].set_title("Unemployment vs Sales")

        plt.tight_layout()

        return self._export_plot()

    # --------------------------------------------------
    # 4️⃣ Anomaly Visualization
    # --------------------------------------------------
    def anomaly_plot(self, store_id: int):

        data = self.df[self.df["Store"] == store_id]
        anom = self.anomalies[self.anomalies["Store"] == store_id]

        plt.figure(figsize=(12, 6))

        plt.plot(data["Date"], data["Weekly_Sales"], label="Sales")
        plt.scatter(anom["Date"], anom["Weekly_Sales"], color="red", label="Anomalies")

        plt.title(f"Sales Anomalies – Store {store_id}")
        plt.legend()

        return self._export_plot()

    # --------------------------------------------------
    # Helper: Return Image
    # --------------------------------------------------
    def _export_plot(self):

        buf = BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close()
        buf.seek(0)

        return StreamingResponse(buf, media_type="image/png")
