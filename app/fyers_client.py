import os
from fyers_api import accessToken, fyersModel

def get_fyers():
    access_token = os.getenv("FYERS_ACCESS_TOKEN")
    client_id = os.getenv("FYERS_CLIENT_ID")
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/tmp/")
    return fyers
