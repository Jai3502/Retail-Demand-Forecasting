import streamlit as st
import requests

st.set_page_config(
   page_title="Retail Forecast Dashboard",
   layout="wide"
)

st.title("Retail Demand Forecasting")

store = st.number_input("Store", 1)

temperature = st.number_input("Temperature")

fuel_price = st.number_input("Fuel Price")

cpi = st.number_input("CPI")

unemployment = st.number_input("Unemployment")

holiday = st.selectbox(
   "Holiday",
   [0, 1]
)

if st.button("Predict Sales"):

   response = requests.post(
       "http://127.0.0.1:8000/predict",
       json={
           "Store": store,
           "Temperature": temperature,
           "Fuel_Price": fuel_price,
           "CPI": cpi,
           "Unemployment": unemployment,
           "Holiday_Flag": holiday,
           "day": 15,
           "month": 6,
           "year": 2025,
           "week": 24,
           "dayofweek": 3,
           "lag_7": 20000,
           "rolling_mean_7": 18000
       }
   )

   result = response.json()

   st.success(
       f"Forecasted Sales: ₹ {result['forecasted_sales']:.2f}"
   )
