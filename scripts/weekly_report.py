import pandas as pd

# Load output files
sharpe = pd.read_csv("outputs/sharpe_ratio.csv")
cagr = pd.read_csv("outputs/cagr_table.csv")
alpha = pd.read_csv("outputs/alpha_beta.csv")

# Top Sharpe Ratio Fund
top_sharpe = sharpe.sort_values(
    "Sharpe_Ratio",
    ascending=False
).head(1)

# Top CAGR Fund (using 5-Year CAGR)
top_cagr = cagr.sort_values(
    "CAGR_5Y",
    ascending=False
).head(1)

# Highest Alpha Fund
top_alpha = alpha.sort_values(
    "Alpha",
    ascending=False
).head(1)

# Create HTML Report
html_content = f"""
<html>
<head>
<title>Weekly Mutual Fund Performance Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
}}
h1 {{
    color: #003366;
}}
h2 {{
    color: #0066cc;
}}
table {{
    border-collapse: collapse;
    width: 80%;
}}
th, td {{
    border: 1px solid #ddd;
    padding: 8px;
}}
th {{
    background-color: #f2f2f2;
}}
</style>
</head>

<body>

<h1>Weekly Mutual Fund Analytics Summary</h1>

<p>Generated from Bluestock Mutual Fund Analytics Platform</p>

<h2>Top Sharpe Ratio Fund</h2>
{top_sharpe.to_html(index=False)}

<h2>Top CAGR Fund (5-Year)</h2>
{top_cagr.to_html(index=False)}

<h2>Highest Alpha Fund</h2>
{top_alpha.to_html(index=False)}

<hr>

<p>
Generated Automatically by:<br>
Bluestock Mutual Fund Analytics Platform
</p>

</body>
</html>
"""

# Save report
with open("outputs/weekly_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Weekly report generated successfully!")
print("Saved to outputs/weekly_report.html")