# TradingView to Fyers Webhook Bot

## Description
Flask-based webhook receiver for TradingView alerts that sends orders to Fyers API.

## Setup
```bash
git clone https://github.com/your/repo.git
cd tradingview-fyers-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Then edit with real credentials
python main.py
