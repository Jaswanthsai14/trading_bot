# Binance Futures Testnet Trading Bot

## Overview

This project is a Python CLI application that places **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**.

It supports both **BUY** and **SELL** orders, validates user input, logs API requests and responses, and handles common errors gracefully.

---

## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API Credentials

Create a `.env` file in the project root.

```env
APIKEY=YOUR_API_KEY
SECRETKEY=YOUR_SECRET_KEY
```

Generate the API credentials from the Binance Futures Testnet.

---

## Running the Application

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Sell Market Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Sell Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logs.py
│   
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Assumptions

- Valid Binance Futures Testnet API credentials are required.
- An internet connection is required to communicate with the Binance Testnet API.
- The application places individual orders only and does not implement any trading strategy.
- API responses are displayed exactly as returned by the Binance Futures Testnet.
