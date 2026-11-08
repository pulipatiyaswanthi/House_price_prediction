# House Price Prediction

An end-to-end Machine Learning project that predicts residential house prices using property-related features. The project includes data analysis, model training, preprocessing, API development and cloud deployment.

## Problem Statement

The objective is to develop a Machine Learning model that predicts house sale prices based on different property characteristics, such as overall quality, living area, garage information, basement area and other housing features.

## Dataset

The dataset contains residential property information and corresponding sale prices.

- Target variable: `SalePrice`
- Features: Property quality, living area, garage details, basement information and other property characteristics.

## Machine Learning Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Hyperparameter Tuning
8. Model Evaluation
9. Model Selection
10. Model Saving
11. FastAPI Integration
12. Cloud Deployment

## Models Evaluated

The following regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost

## Model Evaluation

Models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Best Model

Gradient Boosting Regressor achieved the best performance among the evaluated models.

**R² Score: 0.91**

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- Jupyter Notebook
- Git and GitHub
- Render

## Project Structure

```text
House_price_prediction/
│
├── app/
│   └── main.py
│
├── data/
│   └── raw/
│       └── train.csv
│
├── models/
│   ├── house_price_model.pkl
│   ├── preprocessor.pkl
│   ├── feature_columns.pkl
│   └── model_metrics.pkl
│
├── notebook/
│   └── House_price_prediction.ipynb
│
├── test_api.py
├── test_api_errors.py
├── make_sample.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/pulipatiyaswanthi/House_price_prediction.git
```

Navigate to the project directory:

```bash
cd House_price_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project Locally

### 1. Open the Jupyter Notebook

Open the notebook:

```text
notebook/House_price_prediction.ipynb
```

Run the cells sequentially to explore the dataset, preprocess the data and train the models.

### 2. Start the FastAPI Application

From the project root directory, run:

```bash
uvicorn app.main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

### 3. Open API Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to explore and test the available endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health status |
| GET | `/users/{user_id}` | Retrieve user ID |
| GET | `/houses` | Accept city as a query parameter |
| POST | `/predict` | Predict house price |

### Prediction Workflow

1. User sends house details as JSON.
2. FastAPI validates the input features.
3. The saved preprocessing pipeline transforms the input.
4. The trained Gradient Boosting model predicts the price.
5. The API returns the predicted price as JSON.

## Live Deployment

The FastAPI application is deployed on Render.

- Platform: Render
- Application: House Price Prediction API
- Live API: Add your Render deployment URL here.
- API Documentation: Add your Render `/docs` URL here.

## API Testing

The project includes:

- `test_api.py` – Tests successful house price predictions.
- `test_api_errors.py` – Tests missing and unexpected input features.

The deployed API was tested successfully and returned HTTP 200 for a valid prediction request.

## Future Improvements

- Develop a user-friendly web interface for house price predictions.
- Improve feature engineering and model performance.
- Explore additional regression algorithms.
- Add more comprehensive input validation and monitoring.

## Author

**Yashwanthi Pulipati**

B.Tech – Artificial Intelligence and Data Science