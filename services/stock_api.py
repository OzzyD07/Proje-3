import requests

API_KEY = 'your_alpha_vantage_api_key'

def get_stock_data(symbol):

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "Time Series (Daily)" in data:
        time_series = data["Time Series (Daily)"]
        
        dates = []
        prices = []
        
        for date, daily_data in time_series.items():
            dates.append(date)
            prices.append(float(daily_data['4. close']))
        
        dates.reverse()
        prices.reverse()

        return dates, prices
    else:
        return [], []

