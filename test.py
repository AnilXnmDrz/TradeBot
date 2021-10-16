import os
from binance.client import Client
# api_key = os.environ.get('binance_key')
# api_secret = os.environ.get('binance_secret')


api_key = 'UPpEKdXEnaVs6XnSUjrPaapEzh4F1FSXmYQzDg18e7lLmqmZ1hCLD8D3aX0fwyZR'
api_secret = 'wsw1isN40Z5JQeeDZD9oPth2nOktGRhYgrOYVMerDmQeHZkRQuT0M8I8xMazqmam'

client= Client(api_key,api_secret)
client.API_URL='https://testnet.binance.vision/api'

# print(client.get_account()) #get account detail for every currency

print(client.get_asset_balance(asset="BTC"))  #selective asset info

# print(client.futures_account_balance())