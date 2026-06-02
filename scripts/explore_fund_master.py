import pandas as pd

# Load Fund Master Dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 70)
print("FUND MASTER DATASET EXPLORATION")
print("=" * 70)

# ------------------------------
# Basic Information
# ------------------------------

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDATASET INFO:")
df.info()

# ------------------------------
# Fund House Analysis
# ------------------------------

print("\n" + "=" * 70)
print("FUND HOUSE ANALYSIS")
print("=" * 70)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nTotal Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund House Distribution:")
print(df["fund_house"].value_counts())

# ------------------------------
# Category Analysis
# ------------------------------

print("\n" + "=" * 70)
print("CATEGORY ANALYSIS")
print("=" * 70)

print("\nCategories:")
print(df["category"].unique())

print("\nCategory Distribution:")
print(df["category"].value_counts())

# ------------------------------
# Sub Category Analysis
# ------------------------------

print("\n" + "=" * 70)
print("SUB CATEGORY ANALYSIS")
print("=" * 70)

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nSub Category Distribution:")
print(df["sub_category"].value_counts())

# ------------------------------
# Risk Category Analysis
# ------------------------------

print("\n" + "=" * 70)
print("RISK CATEGORY ANALYSIS")
print("=" * 70)

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nRisk Category Distribution:")
print(df["risk_category"].value_counts())

# ------------------------------
# Fund Manager Analysis
# ------------------------------

print("\n" + "=" * 70)
print("FUND MANAGER ANALYSIS")
print("=" * 70)

print("\nTotal Fund Managers:")
print(df["fund_manager"].nunique())

print("\nTop Fund Managers:")
print(df["fund_manager"].value_counts())

# ------------------------------
# AMFI Code Analysis
# ------------------------------

print("\n" + "=" * 70)
print("AMFI CODE ANALYSIS")
print("=" * 70)

print("\nFirst 20 AMFI Codes:")
print(df["amfi_code"].head(20))

print("\nTotal Unique AMFI Codes:")
print(df["amfi_code"].nunique())

duplicate_codes = df["amfi_code"].duplicated().sum()

print("\nDuplicate AMFI Codes:")
print(duplicate_codes)

# ------------------------------
# Expense Ratio Analysis
# ------------------------------

print("\n" + "=" * 70)
print("EXPENSE RATIO ANALYSIS")
print("=" * 70)

print(df["expense_ratio_pct"].describe())

# ------------------------------
# SIP Analysis
# ------------------------------

print("\n" + "=" * 70)
print("MINIMUM SIP ANALYSIS")
print("=" * 70)

print(df["min_sip_amount"].describe())

# ------------------------------
# Lumpsum Analysis
# ------------------------------

print("\n" + "=" * 70)
print("MINIMUM LUMPSUM ANALYSIS")
print("=" * 70)

print(df["min_lumpsum_amount"].describe())

# ------------------------------
# Final Summary
# ------------------------------

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print("Total Schemes:", len(df))
print("Total Columns:", len(df.columns))
print("Total Fund Houses:", df["fund_house"].nunique())
print("Total Categories:", df["category"].nunique())
print("Total Sub Categories:", df["sub_category"].nunique())
print("Total Fund Managers:", df["fund_manager"].nunique())
print("Total Unique AMFI Codes:", df["amfi_code"].nunique())
print("Duplicate AMFI Codes:", duplicate_codes)

print("\nExploration Completed Successfully.")