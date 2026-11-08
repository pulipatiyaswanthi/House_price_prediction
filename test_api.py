import pandas as pd
import requests
import json
from pathlib import Path

# Locate the original dataset
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "raw" / "train.csv"

# Read one existing house
df = pd.read_csv(DATA_PATH)

house = df.drop(columns=["SalePrice"]).iloc[0]

# Convert house details into JSON-compatible data
house_data = json.loads(house.to_json())

# Send data to FastAPI
response = requests.post(
    "https://house-price-prediction-api-q592.onrender.com/predict",
    json=house_data
)

print("Status Code:", response.status_code)
print("API Response:")
print(response.json())