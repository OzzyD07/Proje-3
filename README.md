<div align="center">

# 📈 Stock Market Tracker

### A Python desktop application for exploring and visualizing stock market data

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-Desktop_GUI-41CD52?style=for-the-badge\&logo=qt\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Alpha Vantage](https://img.shields.io/badge/Alpha_Vantage-Stock_API-blue?style=for-the-badge)

</div>

---

## 📌 About

**Stock Market Tracker** is a desktop application developed with **Python and PyQt6** for retrieving and visualizing stock market data.

Users can create an account, log into the application, search for a stock using its ticker symbol and visualize historical daily closing prices through an interactive chart.

The project demonstrates desktop GUI development, external REST API integration, database-backed authentication and financial data visualization in Python.

---

## ✨ Features

* 🔐 User registration and login
* 📊 Stock market data retrieval
* 🔎 Search stocks using ticker symbols
* 📈 Interactive stock price visualization
* 🗄️ MySQL-based user storage
* 🌐 Alpha Vantage API integration
* 🖥️ Native desktop interface with PyQt6

---

## 🧰 Tech Stack

| Technology                 | Purpose                   |
| -------------------------- | ------------------------- |
| **Python**                 | Application logic         |
| **PyQt6**                  | Desktop user interface    |
| **PyQtGraph**              | Interactive stock charts  |
| **MySQL**                  | User authentication data  |
| **mysql-connector-python** | Python ↔ MySQL connection |
| **Requests**               | HTTP API communication    |
| **Alpha Vantage API**      | Stock market data         |

---

## 🏗️ Project Structure

```text
python-StockMarket/
│
├── login_page.py
│   └── Login & registration interface
│
├── main_page.py
│   └── Main stock tracking interface
│
├── services/
│   ├── db.py
│   │   └── MySQL database connection
│   │
│   └── stock_api.py
│       └── Alpha Vantage API integration
│
└── README.md
```

---

## 🔄 Application Flow

```text
User
 │
 ▼
Login / Registration
 │
 ▼
MySQL Database
 │
 ▼
Stock Search
 │
 ▼
Alpha Vantage API
 │
 ▼
Daily Market Data
 │
 ▼
Interactive Price Chart
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/OzzyD07/python-StockMarket.git
cd python-StockMarket
```

### 2. Install dependencies

```bash
pip install PyQt6 pyqtgraph mysql-connector-python requests
```

---

## 🗄️ Database Configuration

Create a MySQL database named:

```sql
users
```

Configure the connection inside:

```text
services/db.py
```

```python
mysql.connector.connect(
    host="your_host_name",
    user="your_username",
    password="your_password",
    database="users"
)
```

Create the required user table containing the application's username and password fields.

---

## 📡 Alpha Vantage Configuration

Obtain an API key from **Alpha Vantage** and open:

```text
services/stock_api.py
```

Replace:

```python
API_KEY = "your_api_key"
```

with your own API key.

> API keys and database credentials should not be committed to a public repository.

---

## ▶️ Run the Application

Start the application with:

```bash
python login_page.py
```

After launching:

1. Create an account or sign in.
2. Enter a stock ticker such as `AAPL`.
3. Load the stock data.
4. Explore its historical daily closing prices through the chart.

---

## 🎯 Project Focus

This project was built to practice and demonstrate:

**Python desktop development · GUI design · REST API integration · MySQL database connectivity · authentication flows · financial data processing · interactive data visualization**

---

## 👨‍💻 Author

**Ozancan Değirmenci**

[![GitHub](https://img.shields.io/badge/GitHub-OzzyD07-181717?style=for-the-badge\&logo=github)](https://github.com/OzzyD07)

---

<div align="center">

### Built with Python, PyQt6 & Alpha Vantage 📈

</div>
