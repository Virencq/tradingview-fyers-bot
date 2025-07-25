from flask import Flask, request
from dotenv import load_dotenv
from app.webhook_handler import handle_webhook

load_dotenv()  # Load .env file

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    return handle_webhook(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
