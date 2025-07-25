def decide_trade(data):
    # Example: parse from TradingView
    signal = data.get("side")  # e.g., "BUY" or "SELL"
    symbol = data.get("symbol", "NSE:RELIANCE")

    return {
        "symbol": symbol,
        "qty": 1,
        "type": 2,         # Market order
        "side": 1 if signal == "BUY" else -1,
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "disclosedQty": 0,
        "validity": "DAY",
        "offlineOrder": False,
        "stopLoss": 0,
        "takeProfit": 0
    }
