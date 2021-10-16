
import requests
import json
import time
import hmac
import hashlib
baseUrl = 'https://testnet.binance.vision/api/v3/'
APIKEY = '201a0bea210ccf8468e5605711da055c1dd0ff1fbc5d7e18bedd8480a5374b7e'
SECRETKEY = '931509e6e7ef966e1c377ffc6ba1a9dbb6078fe7bf32ccfd89efcc21c24e7aa1'


def makeRequest(url, headers, payload):
    try:
        response = requests.get(url=url, headers=headers, data=payload)
        response.raise_for_status()
        print(response)
        return json.loads(response.text)
    except requests.exceptions.HTTPError as e:
        print(f'error connecting to api {url} ERROR {e}')
    except requests.exceptions.ConnectionError as e:
        print(f'error connecting to api {url} ERROR {e}')
    except requests.exceptions.Timeout as e:
        print(f'error connecting to api {url} ERROR {e}')
    except requests.exceptions.RequestException as e:
        print(f'error connecting to api {url} ERROR')


def exchangeInfo():
    url = baseUrl+'exchangeInfo'
    headers = {'Content-Type': 'application/json'}
    payload = {}
    res = makeRequest(url, headers, payload)
    print(res)


def checkBalance():
    payload = {}
    timestamp = str(time.time())
    # signature = '????????????????????????????????????'
    # url = baseUrl+'account'
    headers = {
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': APIKEY
    }
    signature = hmac.new(bytes(SECRETKEY,'latin-1'), bytes(timestamp,'latin-1'), hashlib.sha256).hexdigest()
    print('signature',signature)
    
    url = baseUrl+'account?timestamp='+timestamp+'&'+'signature='+signature
    res = makeRequest(url, headers, payload)
    print(res)


exchangeInfo()
# checkBalance()
