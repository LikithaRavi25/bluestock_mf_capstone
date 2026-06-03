--dim_fund

CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    category TEXT
);

--dim_date
CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

--fact_nav
CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

--fact_transactions
CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    amount REAL,
    transaction_type TEXT,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

--fact_performance
CREATE TABLE fact_performance (
    perf_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

--fact_aum
CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    aum REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);