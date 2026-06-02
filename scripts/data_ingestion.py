import pandas as pd
from pathlib import Path

files = Path("data/raw").glob("*.csv")

for file in files:
    df = pd.read_csv(file)

    print("\n" + "="*50)
    print("File:", file.name)
    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())