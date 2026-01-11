import streamlit as st
import numpy as np
import pandas as pd
import joblib


st.set_page_config(
    page_title="Bike Demand Prediction",
    page_icon="🚲",
    layout="centered"
)

st.title("🚲 Bike Rental Demand Prediction")
st.markdown("Predict hourly bike demand using weather & time inputs")


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


season_map = {
    "Spring": 1,
    "Summer": 2,
    "Fall": 3,
    "Winter": 4
}

weather_map = {
    "Clear / Few clouds": 1,
    "Mist / Cloudy": 2,
    "Light Snow / Rain": 3,
    "Heavy Rain / Snow": 4
}

binary_map = {"No": 0, "Yes": 1}


st.sidebar.header("📌 Input Parameters")

date = st.sidebar.date_input("Select Date")
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)

season_label = st.sidebar.selectbox("Season", list(season_map.keys()))
weather_label = st.sidebar.selectbox("Weather Condition", list(weather_map.keys()))

holiday_label = st.sidebar.selectbox("Holiday", list(binary_map.keys()))
workingday_label = st.sidebar.selectbox("Working Day", list(binary_map.keys()))

temp = st.sidebar.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
atemp = st.sidebar.number_input("Feels Like Temperature (°C)", 0.0, 50.0, 24.0)
hum = st.sidebar.slider("Humidity (%)", 0, 100, 60)
windspeed = st.sidebar.slider("Wind Speed (km/h)", 0.0, 50.0, 10.0)



season = season_map[season_label]
weathersit = weather_map[weather_label]
holiday = binary_map[holiday_label]
workingday = binary_map[workingday_label]

weekday = date.weekday()
month = date.month
yr = date.year - 2011  


hour_sin = np.sin(2 * np.pi * hour / 24)
hour_cos = np.cos(2 * np.pi * hour / 24)

weekday_sin = np.sin(2 * np.pi * weekday / 7)
weekday_cos = np.cos(2 * np.pi * weekday / 7)

month_sin = np.sin(2 * np.pi * month / 12)
month_cos = np.cos(2 * np.pi * month / 12)

is_weekend = 1 if weekday >= 5 else 0
temp_feel_gap = abs(temp - atemp)
comfort_index = (1 - temp_feel_gap) * (1 - hum / 100)
wind_temp_ratio = windspeed / (temp + 1)

def hour_type_fn(hr):
    if 7 <= hr <= 9 or 17 <= hr <= 19:
        return 2   
    elif 10 <= hr <= 16:
        return 1   
    else:
        return 0  

hour_type = hour_type_fn(hour)


X = pd.DataFrame([[
    season, yr, holiday, workingday, weathersit,
    hum, windspeed,
    hour_sin, hour_cos,
    weekday_sin, weekday_cos,
    month_sin, month_cos,
    is_weekend,
    comfort_index, hour_type, temp_feel_gap, wind_temp_ratio
]], columns=[
    "season", "yr", "holiday", "workingday", "weathersit",
    "hum", "windspeed", "hour_sin", "hour_cos",
    "weekday_sin", "weekday_cos", "month_sin", "month_cos",
    "is_weekend", "comfort_index", "hour_type",
    "temp_feel_gap", "wind_temp_ratio"
])


X_scaled = scaler.transform(X)


st.markdown("---")
if st.button("🔮 Predict Bike Demand"):
    prediction = model.predict(X_scaled)[0]
    st.success(f"🚴 Estimated Bike Demand: **{int(prediction)} bikes**")

    st.info("Prediction is based on historical trends, weather conditions, and time-based patterns.")


st.markdown("---")
st.caption("📊 Powered by Gradient Boosting Regression | Feature Engineered ML Model")
