from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

try:
    from flask_cors import CORS
except ImportError:
    import os
    os.system('pip install flask-cors')
    from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Define a function to get predictions
def predict_stock_prices(symbol, start_date, end_date):
    # Download stock data from Yahoo Finance for the given date range
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    if stock_data.empty:
        raise ValueError("Invalid stock symbol or no data available for the given date range")
    
    # Feature engineering: calculate the number of days since the first date
    stock_data['Days'] = (stock_data.index - stock_data.index[0]).days
    X = stock_data[['Days']]
    y = stock_data['Close']
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate predictions for the next 10 days from the last date in the data
    future_days = np.arange(stock_data['Days'].max() + 1, stock_data['Days'].max() + 11).reshape(-1, 1)
    predicted_prices = model.predict(future_days)
    
    # Create future dates for the next 10 days
    future_dates = pd.date_range(stock_data.index[-1] + pd.Timedelta(days=1), periods=10).strftime('%d-%B-%Y').tolist()
    return future_dates, predicted_prices.tolist()

@app.route('/')
def home():
    return "Stock Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    
    if not symbol or not start_date or not end_date:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    # Convert the start and end date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    try:
        dates, predicted_prices = predict_stock_prices(symbol, start_date, end_date)
        return jsonify({'dates': dates, 'predicted_prices': predicted_prices})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
