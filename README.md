# BLUESTOCK FINTECH
# Mutual Fund Analytics Platform

## Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end data analytics solution developed as part of the Bluestock Fintech Capstone Internship Project.

The project integrates data engineering, financial analytics, and business intelligence techniques to analyze mutual fund performance, investor behavior, portfolio holdings, SIP trends, and benchmark indices.

The solution includes ETL pipelines, SQLite database storage, exploratory data analysis, advanced financial analytics, and interactive Power BI dashboards.

## Project Objectives

- Build an ETL pipeline from raw AMFI data
- Design a normalised SQL schema for MF data
- Perform comprehensive EDA on NAV & AUM data
- Compute performance & risk metrics per scheme
- Build an interactive BI dashboard
- Analyse investor transaction patterns
- Compare fund returns vs benchmark indices
- Document and present the entire project

## Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Power BI |
| Database | SQLite |
| Analytics Environment | Jupyter Notebook |
| Version Control | Git, GitHub |


## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/
│
├── data/
│   ├── raw/
│   ├── processed/
|   ├── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── amfi_validation.py
│   ├── recommender.py
│   ├── verify_counts.py
|   ├── run_pipeline.py
|   ├── load_sqlite.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── outputs/
│
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
├── dashboard/
|   └── bluestock_mf_dashboard.pbix
├── requirements.txt
├── data_dictionary.md
└── README.md
```
## Datasets Used

The project utilizes the following datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

## ETL Pipeline

The project follows a structured ETL workflow:

1. Data Extraction from CSV files
2. Data Cleaning and Validation
3. Feature Engineering
4. Loading into SQLite Database
5. Analytics and Visualization
6. Dashboard Reporting

## Exploratory Data Analysis

Key analyses performed:

- Industry AUM Growth Trend
- Category-wise Net Inflow Analysis
- NAV Correlation Analysis
- Investor Demographics Analysis
- State-wise Investment Analysis
- SIP Growth Trends

## Performance Analytics

The following metrics were calculated:

- CAGR (Compound Annual Growth Rate)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

These metrics help evaluate mutual fund performance and risk-adjusted returns.

## Advanced Analytics

Implemented advanced analytical models including:

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector Concentration Analysis (HHI)
- Rule-Based Fund Recommendation System

## Power BI Dashboard

The dashboard consists of four major pages:

### 1. Industry Overview

- Total Industry AUM
- Monthly SIP Inflows
- Total Folios
- Total Schemes
- Top Fund Houses by AUM

### 2. Fund Performance

- Risk vs Return Analysis
- Fund Performance Scorecard
- NAV Analysis
- Category Filters

### 3. Investor Analytics

- State-wise Investment Distribution
- Age Group Analysis
- Transaction Trends
- Investor Segmentation

### 4. SIP & Market Trends

- SIP Growth Trends
- Category-wise Inflows
- Benchmark Index Trends
- Market Performance Analysis

## Key Findings

- Mutual fund industry AUM showed consistent growth.
- SIP inflows increased significantly over the analysis period.
- Liquid funds attracted the highest inflows.
- Large-cap funds demonstrated stable risk-adjusted performance.
- Investor participation increased across multiple demographics.
- Portfolio concentration varied significantly among schemes.

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/LikithaRavi25/bluestock_mf_capstone
cd BLUESTOCK_MF_CAPSTONE
```
## Live Dashboard

Power BI Dashboard:

 https://app.powerbi.com/links/euz-_AzxHD?ctid=ccdf3676-c077-47cd-ac0f-a253e25e917d&pbi_source=linkShare
### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Run notebooks in the following order:

```text
01_data_ingestion.ipynb
02_data_cleaning.ipynb
03_eda_analysis.ipynb
04_performance_analytics.ipynb
05_advanced_analytics.ipynb
```

## Deliverables

- Final Project Report (PDF)
- Presentation Deck (PPT)
- SQLite Database
- Power BI Dashboard
- Analytics Notebooks
- Advanced Analytics Outputs
- GitHub Repository

## Bonus Features

### Automated ETL Pipeline
Implemented an automated ETL workflow using Python scripts that fetches, cleans, validates, and loads mutual fund data into SQLite.

### Streamlit Dashboard
Developed a lightweight web dashboard using Streamlit as an alternative interface to Power BI visualizations.

### Monte Carlo NAV Projection
Performed Monte Carlo simulations to forecast future NAV growth trajectories under uncertainty and market volatility.

### Portfolio Optimization
Implemented Markowitz Mean-Variance Portfolio Optimization and generated an Efficient Frontier for optimal asset allocation.

### Automated Weekly Report Generator
Built an HTML-based reporting system that automatically generates weekly mutual fund performance summaries.

## Author

**Likitha R**

B.Tech – Computer Science and Engineering

Data Analyst Intern

Blustock Fintech

## License

This project was developed for educational and internship purposes as part of the Bluestock Fintech Capstone Project.