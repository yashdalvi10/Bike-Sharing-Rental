🚲 Bike Rental Demand Prediction
An end-to-end machine learning regression project to predict bike rental demand using Gradient Boosting (Tuned) with advanced feature engineering, model evaluation, and deployment-ready architecture.


📌 Project Overview
Accurate demand forecasting helps bike rental companies optimize inventory, reduce operational costs, and improve customer satisfaction.
This project predicts the number of bike rentals based on time, weather, and engineered features.


🧠 Model Used
Gradient Boosting Regressor (Tuned)
Final Performance:
- R² Score: 0.9356
- RMSE: 24.38
- MAE: 14.99


🛠️ Feature Engineering
✅ Final Features Used
- season, yr, holiday, workingday, weathersit,
- hum, windspeed,
- hour_sin, hour_cos,
- weekday_sin, weekday_cos,
- month_sin, month_cos,
- is_weekend,
- comfort_index,
- hour_type,
- temp_feel_gap,
- wind_temp_ratio



📊 Visualizations Included

- 📈 Actual vs Predicted plot
- 📉 Residual error plot
- 🧠 Feature importance plot
- 📊 Confidence interval display



🚀 Deployment Ready

- Streamlit App for user-friendly interaction

- StandardScaler applied for consistent input scaling

- Pickle (.pkl) model saved for inference

- Docker support for easy cloud deployment



🐳 Docker Support

Docker allows:
- Consistent environment across systems
- Easy cloud deployment (AWS / Azure / GCP)
- Fast setup with zero dependency issues


▶️ How to Run Locally

1️⃣ Install dependencies
- pip install -r requirements.txt

2️⃣ Run Streamlit app
- streamlit run app.py

🐳 Run Using Docker
- docker build -t bike-demand-app .
- docker run -p 8501:8501 bike-demand-app



🔮 Future Enhancements

- Deep Learning models (LSTM)
- Real-time weather API integration=
- Model monitoring & drift detection
- CI/CD pipeline for production



👨‍💻 Author

Yash Dalvi
Machine Learning Developer
- Mail: ydalvi565@gmail.com
- Mobile No.: 8805946804
