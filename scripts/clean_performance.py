import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Remove rows with missing values
df = df.dropna()

# Expense Ratio Validation
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# Morningstar Rating Validation
df = df[
    (df["morningstar_rating"] >= 1)
    &
    (df["morningstar_rating"] <= 5)
]

# Risk Grade Validation
valid_risk = [
    "Low",
    "Moderate",
    "High",
    "Very High"
]

df = df[
    df["risk_grade"].isin(valid_risk)
]

# Flag anomalies
df["anomaly"] = (
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -50) |
    (df["return_3yr_pct"] > 100) |
    (df["return_3yr_pct"] < -50) |
    (df["return_5yr_pct"] > 150) |
    (df["return_5yr_pct"] < -50)
)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned successfully")
print("Rows:", len(df))
print("Anomalies:", df["anomaly"].sum())