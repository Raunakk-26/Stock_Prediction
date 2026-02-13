# Stock_Prediction
# 📈 Stock Price Prediction using Live Market Data

## 🚀 Project Overview

This project is a complete end-to-end machine learning web application designed to predict stock price trends using live and historical market data. It demonstrates the full ML pipeline — from data collection and preprocessing to model training, evaluation, and deployment through a Flask-based web interface.

The system allows users to select a stock, analyze historical performance, and generate predictions for future price movements. The goal is to build a practical, production-style ML project that showcases real-world data handling, feature engineering, model evaluation, and deployment.

## 🎯 Objectives

* Predict future stock price trends using historical data
* Build a full ML pipeline with real-time data integration
* Deploy a trained model via a web interface
* Visualize predictions for interpretability
* Demonstrate industry-relevant skills in ML + Backend + UI integration

## ✨ Key Features

* 📊 Live stock data collection using Alpha Vantage API
* 🧹 Data cleaning and preprocessing pipeline
* 🧠 Feature engineering using time-based indicators
* 📉 Linear Regression model for trend prediction
* 📈 Visualization of actual vs predicted stock prices
* 🌐 Flask backend serving real-time predictions
* 🖥️ Interactive web UI for user input and results display

## 🧠 Machine Learning Pipeline

The system follows a structured ML workflow:

1. **Data Collection**

   * Fetches real-time and historical stock data using Alpha Vantage API
   * Stores time-series price data

2. **Data Preprocessing**

   * Handles missing values
   * Date-based filtering
   * Converts raw data into model-ready format

3. **Feature Engineering**

   * Time-based features (day, month trends)
   * Historical price patterns
   * Trend-based signal extraction

4. **Model Training**

   * Algorithm used: Linear Regression
   * Learns relationships between historical price patterns and future movement

5. **Evaluation**

   * Metric: RMSE (Root Mean Squared Error)
   * Analyzes prediction reliability and model behavior

6. **Prediction**

   * Generates future stock price values
   * Extrapolates trends from learned historical patterns

7. **Deployment**

   * Model served via Flask API
   * Predictions displayed in a browser-based dashboard

## 🛠️ Tech Stack

### Programming & ML

* Python
* Pandas
* NumPy
* scikit-learn

### Backend

* Flask
* REST API integration

### Frontend

* HTML
* CSS
* JavaScript

### Data Source

* Alpha Vantage API

## 📁 Project Structure

```
Stock-Price-Prediction/
│
├── app.py                  # Flask server and routing
├── ml_model.py             # Training and prediction logic
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── models/
│   └── trained_model.pkl
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add Alpha Vantage API Key

Create a `.env` file or directly add in code:

```
API_KEY=YOUR_API_KEY
```

### 4️⃣ Run Application

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

## 📊 Model Details

* Model Type: Linear Regression
* Problem Type: Time-Series Trend Prediction
* Input Data: Historical stock price data
* Output: Predicted future price values
* Evaluation Metric: RMSE

## 📈 Example Workflow

1. User selects a stock ticker
2. System fetches historical price data
3. Data is cleaned and processed
4. Model generates predictions
5. Results displayed with visualization

## 💡 What This Project Demonstrates

* Real-world ML problem solving
* API integration with live data
* End-to-end ML lifecycle implementation
* Backend deployment with Flask
* Data visualization for interpretability
* Strong portfolio-level project structure

## 🔮 Future Improvements

* Add LSTM / Deep Learning models for better accuracy
* Support multiple stock comparisons
* Add technical indicators (RSI, MACD, Moving Averages)
* Improve UI with interactive charts
* Deploy on cloud (AWS / Render / Railway)

## 👨‍💻 Author

**Raunak Das**
GitHub: https://github.com/Raunakk-26
LinkedIn: https://linkedin.com/in/theraunakk/
