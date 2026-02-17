# Anomaly Detection service module
import numpy as np

class AnomalyService:

    def __init__(self, df):
        self.df = df

    def zscore(self, threshold=3):

        z = np.abs((self.df["Weekly_Sales"] -
            self.df["Weekly_Sales"].mean()) /
            self.df["Weekly_Sales"].std())

        a = self.df[z > threshold].copy()
        a["reason"] = "zscore"

        return a[["Store","Date","Weekly_Sales","reason"]]

    def iqr(self):

        q1 = self.df.Weekly_Sales.quantile(.25)
        q3 = self.df.Weekly_Sales.quantile(.75)

        iqr = q3-q1

        a = self.df[(self.df.Weekly_Sales<q1-1.5*iqr)|
                    (self.df.Weekly_Sales>q3+1.5*iqr)].copy()

        a["reason"] = "iqr"

        return a[["Store","Date","Weekly_Sales","reason"]]
