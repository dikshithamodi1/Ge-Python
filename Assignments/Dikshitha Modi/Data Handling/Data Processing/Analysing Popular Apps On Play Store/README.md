Google Play Store Popularity Analysis
Overview

This project analyzes the Google Play Store dataset to understand what drives app popularity using data cleaning, exploratory data analysis (EDA), and feature engineering.

🛠 Tech Stack

Python

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

 Data Processing

Removed duplicates and handled missing values

Cleaned Installs, Price, and Size columns

Converted Last Updated to datetime

Removed invalid rating values

Final dataset: 10,358 apps × 13 features

📊 Key Analysis

Rating distribution

Category-wise installs

Revenue estimation (Installs × Price)

Correlation analysis

App age analysis

Free vs Paid comparison

Popular App Identification

Apps were analyzed using:

Highest Installs

Top app per category

Top 10% apps (data-driven threshold)

Custom Popularity Score

Popularity Score Formula:
0.5 × Installs +
0.3 × Reviews +
0.2 × Rating


(Normalized before weighting)

Key Insights

Reviews strongly correlate with installs.

Rating has weak correlation with installs.

Free apps dominate downloads.

A few apps dominate installs within categorie