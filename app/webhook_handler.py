from flask import jsonify
from app.fyers_client import get_fyers
from app.strategy_logic import decide_trade

def handle_webhook(data):
    try:
        order_data = decide_trade(data)
        fyers = get_fyers()
        response = fyers.place_order(order_data)
        return jsonify({'status': 'success', 'fyers_response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
