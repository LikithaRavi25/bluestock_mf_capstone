import requests
import pandas as pd
from pathlib import Path


codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

all_data = []

for code in codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    all_data.append({
        "scheme_code": code,
        "scheme_name": data["meta"]["scheme_name"]
    })

df = pd.DataFrame(all_data)
Path("data/raw").mkdir(parents=True, exist_ok=True)



df.to_csv("data/raw/key_funds.csv", index=False)
print(df)