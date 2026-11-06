import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "data" / "raw" / "train.csv")

# Select one house and remove its actual selling price
sample_house = df.drop(columns=["SalePrice"]).iloc[0]

# Convert to JSON-compatible dictionary
sample_data = json.loads(sample_house.to_json())

# Save JSON file
with open(BASE_DIR / "sample_house.json", "w") as file:
    json.dump(sample_data, file, indent=4)

print("Sample JSON created successfully!")
print("Number of features:", len(sample_data))