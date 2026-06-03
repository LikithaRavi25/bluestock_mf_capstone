import pandas as pd
import sqlite3

# Connect database
conn = sqlite3.connect("bluestock_mf.db")

# CSV row counts
nav_csv = len(pd.read_csv(
    "data/processed/nav_history_clean.csv"
))

txn_csv = len(pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
))

perf_csv = len(pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
))

# Database row counts
nav_db = pd.read_sql(
    "SELECT COUNT(*) as count FROM fact_nav",
    conn
)["count"][0]

txn_db = pd.read_sql(
    "SELECT COUNT(*) as count FROM fact_transactions",
    conn
)["count"][0]

perf_db = pd.read_sql(
    "SELECT COUNT(*) as count FROM fact_performance",
    conn
)["count"][0]

print("NAV")
print("CSV:", nav_csv)
print("DB :", nav_db)

print("\nTransactions")
print("CSV:", txn_csv)
print("DB :", txn_db)

print("\nPerformance")
print("CSV:", perf_csv)
print("DB :", perf_db)

conn.close()