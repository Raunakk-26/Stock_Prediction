from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)
CORS(app)

API_KEY = 'IO3ZT4YBQMDVIACI'  # Replace this with your Alpha Vantage API key

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not symbol or not start_date or not end_date:
        return jsonify({'error': 'Missing input parameters'}), 400

    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=full'
        response = requests.get(url)
        json_data = response.json()

        if 'Time Series (Daily)' not in json_data:
            return jsonify({'error': 'Invalid stock symbol or API limit reached'}), 400

        time_series = json_data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df = df.rename(columns={'4. close': 'Close'})
        df['Close'] = df['Close'].astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df = df.loc[start_date:end_date]

        if df.empty:
            return jsonify({'error': 'No data available for selected date range'}), 400

        df['Days'] = (df.index - df.index[0]).days
        model = LinearRegression()
        model.fit(df[['Days']], df['Close'])

        future_days = np.arange(df['Days'].max() + 1, df['Days'].max() + 11).reshape(-1, 1)
        predicted_prices = model.predict(future_days)
        future_dates = pd.date_range(df.index[-1] + timedelta(days=1), periods=10).strftime('%d-%B-%Y').tolist()

        return jsonify({'dates': future_dates, 'predicted_prices': predicted_prices.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
