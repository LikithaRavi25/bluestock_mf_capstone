import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data)

df = pd.DataFrame([data])

df.to_csv("../data/raw/live_nav.csv", index=False)

print("Saved Successfully")