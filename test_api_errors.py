import pandas as pd
import requests
import json

API_URL = "https://house-price-prediction-api-q592.onrender.com/predict"

# Load sample house details
df = pd.read_csv("data/raw/train.csv")

house_row = df.drop(columns=["SalePrice"]).iloc[0]

# Convert NaN values into JSON-compatible null values
house = json.loads(house_row.to_json())

# Test 1: Missing feature
missing_house = house.copy()
missing_house.pop("LotArea")

response = requests.post(API_URL, json=missing_house)

print("\nTEST 1: Missing Feature")
print("Status Code:", response.status_code)
print("Response:", response.json())


# Test 2: Unexpected feature
extra_house = house.copy()
extra_house["unexpected_feature"] = 100

response = requests.post(API_URL, json=extra_house)

print("\nTEST 2: Unexpected Feature")
print("Status Code:", response.status_code)
print("Response:", response.json())