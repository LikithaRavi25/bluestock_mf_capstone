import pandas as pd

# 1. Fund Master

df = pd.read_csv("data/raw/01_fund_master.csv")

df = df.drop_duplicates()

df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

df.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print("Fund Master cleaned")


# 2. AUM by Fund House

df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.drop_duplicates()

df = df[df["aum_crore"] > 0]

df.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)

print("AUM cleaned")


# 3. SIP Inflows

df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)

print("SIP cleaned")


# 4. Category Inflows

df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

df = df.drop_duplicates()

df["category"] = (
    df["category"]
      .str.strip()
      .str.title()
)

df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print("Category Inflows cleaned")


# 5. Industry Folio Count

df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print("Folio Count cleaned")


# 6. Portfolio Holdings

df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

df = df.drop_duplicates()

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

df = df[
    (df["weight_pct"] >= 0)
    &
    (df["weight_pct"] <= 100)
]

df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio cleaned")


# 7. Benchmark Indices

df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.drop_duplicates()

df = df[df["close_value"] > 0]

df.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)

print("Benchmark cleaned")


