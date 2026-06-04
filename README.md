# Retail Demand Forecasting & Inventory Optimization System

##  Project Overview

Retail Demand Forecasting & Inventory Optimization System is a Machine Learning project designed to predict future product demand and help retailers optimize inventory management. The system analyzes historical sales data, performs feature engineering, trains forecasting models, and provides accurate demand predictions.

##  Features

* Data Ingestion Pipeline
* Data Validation
* Data Transformation
* Feature Engineering
* Demand Forecasting using XGBoost
* Inventory Optimization Support
* FastAPI Backend
* Streamlit Frontend
* Model Training & Evaluation
* Automated Prediction Pipeline

##  Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Streamlit
* Joblib
* Git & GitHub

##  Project Structure

```text
Retail-Demand-Forecasting
│
├── artifacts/
│   ├── models/
│   ├── scaler/
│   └── reports/
│
├── frontend/
│   └── streamlit_app.py
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│   └── api/
│
├── requirements.txt
├── README.md
└── main.py
```

##  Installation

### Clone Repository

```bash
git clone https://github.com/Jai3502/Retail-Demand-Forecasting.git
cd Retail-Demand-Forecasting
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

##  Train Model

```bash
python -m src.pipeline.training_pipeline
```

##  Run FastAPI Backend

```bash
uvicorn src.api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

##  Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

##  Model Performance

* Algorithm: XGBoost Regressor
* Evaluation Metric: MAE (Mean Absolute Error)
* Trained model saved in:

  * artifacts/models/xgboost.pkl
  * artifacts/models/model_columns.pkl

##  Future Enhancements

* Real-time Demand Forecasting
* Advanced Inventory Optimization
* Cloud Deployment
* Interactive Dashboard
* Automated Retraining Pipeline

##  Author

**Jai Prakash**

GitHub: https://github.com/Jai3502

---

⭐ If you found this project useful, please give it a star on GitHub.
