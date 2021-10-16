import os
from binance.client import Client
from time import sleep
from binance import ThreadedWebsocketManager

# api_key = os.environ.get('binance_key')
# api_secret = os.environ.get('binance_secret')


<<<<<<< HEAD
api_key = '201a0bea210ccf8468e5605711da055c1dd0ff1fbc5d7e18bedd8480a5374b7e'
api_secret = '931509e6e7ef966e1c377ffc6ba1a9dbb6078fe7bf32ccfd89efcc21c24e7aa1'

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'
client= Client(api_key,api_secret,testnet=True)

# print(client.get_account()) #get account detail for every currency

print(client.get_asset_balance(asset="BTC"))  # selective asset info

# print(client.futures_account_balance())
=======
# api_key = 'UPpEKdXEnaVs6XnSUjrPaapEzh4F1FSXmYQzDg18e7lLmqmZ1hCLD8D3aX0fwyZR'
# api_secret = 'wsw1isN40Z5JQeeDZD9oPth2nOktGRhYgrOYVMerDmQeHZkRQuT0M8I8xMazqmam'
api_key = '4e1c61706c288ae1923844db22f1464d2f7ebdfcec39f496e4344ba80e8c3d26'
api_secret = '99b4eb73ba3dc0764a49fdf7ec2214aef388bd3b57a957ea03a62a202a4e9108'

client= Client(api_key,api_secret,testnet=True)
# client.API_URL='https://testnet.binance.vision/api'
client.API_URL='https://testnet.binancefuture.com'

# print(client.get_account()) #get account detail for every currency

# print(client.get_asset_balance(asset="BTC"))  #selective asset info

# print(client.futures_account_balance())
# print(client.get_symbol_ticker(symbol="BTCUSDT")) #latest price for symbol

btc_price = {'error':False}
def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
	    print(msg['c'])
	    btc_price['last'] = msg['c']
	    btc_price['bid'] = msg['b']
	    btc_price['last'] = msg['a']
	    btc_price['error'] = False
    else:
        btc_price['error'] = True
        
bsm = ThreadedWebsocketManager()
bsm.start()
# subscribe to a stream
i=0
while i<2:
    bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')
    sleep(3000)
    i+=1
    print('btc price',btc_price)
    if i==1:
        bsm.stop()
        
>>>>>>> 5a12980984e9c2fa0b675bffb3a289594c5d3254
