import os
from binance.client import Client
# api_key = os.environ.get('binance_key')
# api_secret = os.environ.get('binance_secret')


api_key = '201a0bea210ccf8468e5605711da055c1dd0ff1fbc5d7e18bedd8480a5374b7e'
api_secret = '931509e6e7ef966e1c377ffc6ba1a9dbb6078fe7bf32ccfd89efcc21c24e7aa1'

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'
client= Client(api_key,api_secret,testnet=True)

# print(client.get_account()) #get account detail for every currency

print(client.get_asset_balance(asset="BTC"))  # selective asset info

# print(client.futures_account_balance())
