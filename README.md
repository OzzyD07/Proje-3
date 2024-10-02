# Stock Market Tracker

This is a PyQt6-based desktop application that allows users to track stock market data. The application features a login system and real-time stock data visualization.

## Features

- User authentication (login and registration)
- Real-time stock data retrieval
- Interactive stock price chart
- User-friendly GUI

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- PyQt6
- pyqtgraph
- mysql-connector-python
- requests

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/OzzyD07/PROJE-3.git

2. Navigate to the project directory:
   ```
   cd PROJE-3
   ```

3. Install the required packages:
   ```
   pip install PyQt6 pyqtgraph mysql-connector-python requests
   ```

4. Set up the MySQL database:
   - Create a database named `users`
   - Create a table named `users` with columns `userName` and `password`

5. Update the database connection details in `services/db.py`

6. Get an API key from Alpha Vantage and update it in `services/stock_api.py`

## Usage

To run the application:

```
python login_page.py
```

1. Register a new account or log in with existing credentials
2. Enter a stock symbol (e.g., AAPL for Apple Inc.)
3. Click "Load Stock Data" to view the stock's price chart

## Project Structure

- `login_page.py`: Contains the login and registration UI
- `main_page.py`: Contains the main stock tracking UI
- `services/db.py`: Handles database connections
- `services/stock_api.py`: Handles stock data retrieval from Alpha Vantage API

## Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for providing the stock market data API
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework
- [pyqtgraph](http://www.pyqtgraph.org/) for the interactive plotting