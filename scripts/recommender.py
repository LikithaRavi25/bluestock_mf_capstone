import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)
print(df["risk_grade"].unique())

def recommend_funds(risk_appetite):

    filtered = df[
        df["risk_grade"]
        .str.contains(
            risk_appetite,
            case=False,
            na=False
        )
    ]

    top3 = (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return top3[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

recommendations = recommend_funds(risk)

print("\nTop Recommended Funds:\n")

print(recommendations)