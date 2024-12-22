import os
import requests
from dotenv import load_dotenv

def get_exchange(currency):
    ''' Функция возвращает курс валюты которую подали в функцию относительно British Pound'''
    load_dotenv()
    my_api =os.getenv("ApiKey_ninjas")
    currency_pair =currency+'_GBP'

    api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={currency_pair}'
    response = requests.get(api_url, headers={'X-Api-Key': my_api})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return f'Error:, {response.status_code}, {response.text}'


def get_stock_prices(stock):
    load_dotenv()
    my_api = os.getenv("ApiKey_ninjas")

    api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(stock)
    response = requests.get(api_url, headers={'X-Api-Key': my_api})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
       return f'Error:, {response.status_code}, {response.text}'



'''
{'ticker': 'AAPL', 'name': 'Apple Inc.', 'price': 254.49, 'exchange': 'NASDAQ', 'updated': 1734728403, 'currency': 'USD'}
{'ticker': 'AMZN', 'name': 'Amazon.com, Inc.', 'price': 224.92, 'exchange': 'NASDAQ', 'updated': 1734728403, 'currency': 'USD'}
{'currency_pair': 'CNY_GBP', 'exchange_rate': 0.109063}
{'currency_pair': 'CHF_GBP', 'exchange_rate': 0.890234}
{'currency_pair': 'DKK_GBP', 'exchange_rate': 0.111271}
'''
