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


