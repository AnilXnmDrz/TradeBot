
import requests
import json
import time
baseUrl = 'https://testnet.binance.vision/api/v3/'
APIKEY = 'UPpEKdXEnaVs6XnSUjrPaapEzh4F1FSXmYQzDg18e7lLmqmZ1hCLD8D3aX0fwyZR'
SECRETKEY = 'wsw1isN40Z5JQeeDZD9oPth2nOktGRhYgrOYVMerDmQeHZkRQuT0M8I8xMazqmam'


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
    signature = '????????????????????????????????????'
    url = baseUrl+'account?timestamp='+timestamp+'&'+'signature='+signature
    url = baseUrl+'account'
    headers = {
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': APIKEY
    }
    res = makeRequest(url, headers, payload)
    print(res.text)


exchangeInfo()
# checkBalance()
