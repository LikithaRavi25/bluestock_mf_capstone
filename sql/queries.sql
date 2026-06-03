--top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

--Average NAV per month
SELECT
strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

--sip yoy growth
SELECT
strftime('%Y',transaction_date),
SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY 1;

--expense ratio<1
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

--transactions by state
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

--highest NAV
SELECT MAX(nav)
FROM fact_nav;

--lowest NAV
SELECT MIN(nav)
FROM fact_nav;

--total sip amount
SELECT SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP';

--average return
SELECT AVG(return_1y)
FROM fact_performance;

--total funds
SELECT COUNT(DISTINCT amfi_code)
FROM fact_nav;