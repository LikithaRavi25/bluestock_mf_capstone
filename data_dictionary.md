# DATA DICTIONARY

## 1. Fund Master Dataset

**Source:** `01_fund_master.csv`

| Column             | Data Type | Description                                             |
| ------------------ | --------- | ------------------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI code identifying the mutual fund scheme     |
| fund_house         | TEXT      | Asset Management Company (AMC) managing the fund        |
| scheme_name        | TEXT      | Name of the mutual fund scheme                          |
| category           | TEXT      | Broad category of the fund (Equity, Debt, Hybrid, etc.) |
| sub_category       | TEXT      | Specific sub-category within the fund category          |
| plan               | TEXT      | Plan type such as Direct or Regular                     |
| launch_date        | DATE      | Date on which the scheme was launched                   |
| benchmark          | TEXT      | Benchmark index used for fund performance comparison    |
| expense_ratio_pct  | FLOAT     | Annual expense ratio charged by the fund (%)            |
| exit_load_pct      | FLOAT     | Exit load charged on redemption (%)                     |
| min_sip_amount     | FLOAT     | Minimum amount required for SIP investment              |
| min_lumpsum_amount | FLOAT     | Minimum amount required for lump sum investment         |
| fund_manager       | TEXT      | Name of the fund manager managing the scheme            |
| risk_category      | TEXT      | Risk level associated with the scheme                   |
| sebi_category_code | TEXT      | SEBI classification code for the scheme                 |


## 2. NAV History Dataset

**Source:** `02_nav_history.csv`

| Column    | Data Type | Description                                                    |
| --------- | --------- | -------------------------------------------------------------- |
| amfi_code | INTEGER   | Unique AMFI code identifying the mutual fund scheme            |
| date      | DATE      | Date for which the NAV is recorded                             |
| nav       | FLOAT     | Net Asset Value (NAV) of the mutual fund on the specified date |

## 3. AUM By Fund House Dataset

**Source:** `03_aum_by_fund_house.csv`

| Column         | Data Type | Description                                             |
| -------------- | --------- | ------------------------------------------------------- |
| date           | DATE      | Date on which the AUM data was recorded                 |
| fund_house     | TEXT      | Asset Management Company (AMC) name                     |
| aum_lakh_crore | FLOAT     | Total Assets Under Management expressed in lakh crores  |
| aum_crore      | FLOAT     | Total Assets Under Management expressed in crores       |
| num_schemes    | INTEGER   | Number of mutual fund schemes managed by the fund house |

## 4. Monthly SIP Inflows Dataset

**Source:** `04_monthly_sip_inflows.csv`

| Column                    | Data Type | Description                                                      |
| ------------------------- | --------- | ---------------------------------------------------------------- |
| month                     | DATE/TEXT | Month for which SIP statistics are reported                      |
| sip_inflow_crore          | FLOAT     | Total SIP inflows received during the month (in crores)          |
| active_sip_accounts_crore | FLOAT     | Number of active SIP accounts (in crores)                        |
| new_sip_accounts_lakh     | FLOAT     | Number of newly registered SIP accounts (in lakhs)               |
| sip_aum_lakh_crore        | FLOAT     | Assets Under Management through SIP investments (in lakh crores) |
| yoy_growth_pct            | FLOAT     | Year-over-Year growth percentage in SIP investments              |

## 5. Category Inflows Dataset

**Source:** `05_category_inflows.csv`

| Column           | Data Type | Description                                                                  |
| ---------------- | --------- | ---------------------------------------------------------------------------- |
| month            | DATE/TEXT | Month for which inflow data is reported                                      |
| category         | TEXT      | Mutual fund category (Equity, Debt, Hybrid, etc.)                            |
| net_inflow_crore | FLOAT     | Net inflow or outflow of funds for the category during the month (in crores) |

## 6. Industry Folio Dataset

**Source:** `06_industry_folio_count.csv`

| Column              | Data Type | Description                                                  |
| ------------------- | --------- | ------------------------------------------------------------ |
| month               | DATE/TEXT | Month for which folio statistics are reported                |
| total_folios_crore  | FLOAT     | Total number of mutual fund folios (in crores)               |
| equity_folios_crore | FLOAT     | Number of equity mutual fund folios (in crores)              |
| debt_folios_crore   | FLOAT     | Number of debt mutual fund folios (in crores)                |
| hybrid_folios_crore | FLOAT     | Number of hybrid mutual fund folios (in crores)              |
| others_folios_crore | FLOAT     | Number of folios in other mutual fund categories (in crores) |

## 7. Scheme Performance Dataset

**Source:** `07_scheme_performance.csv`

| Column             | Data Type | Description                                                    |
| ------------------ | --------- | -------------------------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI code identifying the mutual fund scheme            |
| scheme_name        | TEXT      | Name of the mutual fund scheme                                 |
| fund_house         | TEXT      | Asset Management Company (AMC) managing the fund               |
| category           | TEXT      | Category of the mutual fund scheme                             |
| plan               | TEXT      | Plan type such as Direct or Regular                            |
| return_1yr_pct     | FLOAT     | Annual return generated over the last 1 year (%)               |
| return_3yr_pct     | FLOAT     | Annualized return generated over the last 3 years (%)          |
| return_5yr_pct     | FLOAT     | Annualized return generated over the last 5 years (%)          |
| benchmark_3yr_pct  | FLOAT     | 3-year return of the benchmark index (%)                       |
| alpha              | FLOAT     | Excess return generated by the fund compared to its benchmark  |
| beta               | FLOAT     | Measure of the fund's volatility relative to the market        |
| sharpe_ratio       | FLOAT     | Risk-adjusted return metric                                    |
| sortino_ratio      | FLOAT     | Downside risk-adjusted return metric                           |
| std_dev_ann_pct    | FLOAT     | Annualized standard deviation representing fund volatility (%) |
| max_drawdown_pct   | FLOAT     | Maximum observed loss from a peak to a trough (%)              |
| aum_crore          | FLOAT     | Assets Under Management (AUM) of the scheme in crores          |
| expense_ratio_pct  | FLOAT     | Annual expense ratio charged by the fund (%)                   |
| morningstar_rating | INTEGER   | Morningstar rating assigned to the scheme (1–5)                |
| risk_grade         | TEXT      | Risk classification of the scheme                              |

## 8. Investor Transactions Dataset

**Source:** `08_investor_transactions.csv`

| Column             | Data Type | Description                                           |
| ------------------ | --------- | ----------------------------------------------------- |
| investor_id        | INTEGER   | Unique identifier for the investor                    |
| transaction_date   | DATE      | Date on which the transaction was made                |
| amfi_code          | INTEGER   | Unique AMFI code identifying the mutual fund scheme   |
| transaction_type   | TEXT      | Type of transaction (SIP, Lumpsum, Redemption, etc.)  |
| amount_inr         | FLOAT     | Transaction amount in Indian Rupees (INR)             |
| state              | TEXT      | State of residence of the investor                    |
| city               | TEXT      | City of residence of the investor                     |
| city_tier          | TEXT      | Classification of city (Tier 1, Tier 2, Tier 3, etc.) |
| age_group          | TEXT      | Investor age category                                 |
| gender             | TEXT      | Gender of the investor                                |
| annual_income_lakh | FLOAT     | Annual income of the investor (in lakhs)              |
| payment_mode       | TEXT      | Mode of payment used for the transaction              |
| kyc_status         | TEXT      | Know Your Customer (KYC) verification status          |

## 9. Portfolio Holdings Dataset

**Source:** `09_portfolio_holdings.csv`

| Column            | Data Type | Description                                               |
| ----------------- | --------- | --------------------------------------------------------- |
| amfi_code         | INTEGER   | Unique AMFI code identifying the mutual fund scheme       |
| stock_symbol      | TEXT      | Stock ticker symbol                                       |
| stock_name        | TEXT      | Name of the company/security held in the portfolio        |
| sector            | TEXT      | Industry sector to which the stock belongs                |
| weight_pct        | FLOAT     | Percentage weight of the stock in the fund portfolio      |
| market_value_cr   | FLOAT     | Market value of the holding in crores                     |
| current_price_inr | FLOAT     | Current market price of the stock in INR                  |
| portfolio_date    | DATE      | Date on which the portfolio holding snapshot was recorded |

## 10. Benchmark Indices Dataset

**Source:** `10_benchmark_indices.csv`

| Column      | Data Type | Description                                                |
| ----------- | --------- | ---------------------------------------------------------- |
| date        | DATE      | Date on which the index value was recorded                 |
| index_name  | TEXT      | Name of the benchmark index                                |
| close_value | FLOAT     | Closing value of the benchmark index on the specified date |













