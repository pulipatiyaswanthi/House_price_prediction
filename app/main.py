from fastapi import FastAPI, HTTPException
from fastapi import Body
import joblib
import pandas as pd
from pathlib import Path

# Initialize FastAPI
app = FastAPI(title="House Price Prediction API")

# --------------------------------------------------
# 1. LOAD SAVED ML FILES
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

try:
    preprocessor = joblib.load(MODEL_DIR / "preprocessor.pkl")
    model = joblib.load(MODEL_DIR / "house_price_model.pkl")
    feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")

    print("ML model loaded successfully!")
    print("Preprocessor loaded successfully!")

except Exception as e:
    raise RuntimeError(f"Error loading ML files: {e}")


# --------------------------------------------------
# 2. HOME ENDPOINT
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}


# --------------------------------------------------
# 3. HEALTH ENDPOINT
# --------------------------------------------------

@app.get("/health")
def health():
    return {"status": "healthy"}


# --------------------------------------------------
# 4. USERS ENDPOINT
# --------------------------------------------------

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# --------------------------------------------------
# 5. HOUSES ENDPOINT
# --------------------------------------------------

@app.get("/houses")
def get_houses(city: str):
    return {"city": city}


# --------------------------------------------------
# 6. HOUSE PRICE PREDICTION ENDPOINT
# --------------------------------------------------

@app.post("/predict")
def predict(house: dict = Body(...)):

    try:
        # Check missing features
        missing_features = [
            col for col in feature_columns if col not in house
        ]

        # Check unexpected features
        extra_features = [
            col for col in house if col not in feature_columns
        ]

        if missing_features or extra_features:
            raise HTTPException(
                status_code=400,
                detail={
                    "missing_features": missing_features,
                    "unexpected_features": extra_features
                }
            )

        # Convert input into DataFrame
        input_df = pd.DataFrame(
            [house],
            columns=feature_columns
        )

        # Apply saved preprocessing
        transformed_data = preprocessor.transform(input_df)

        # Predict house price
        prediction = model.predict(transformed_data)

        # Return prediction
        return {
            "predicted_house_price": round(float(prediction[0]), 2)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )