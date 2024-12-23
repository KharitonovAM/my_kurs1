import os
import requests
from dotenv import load_dotenv
from logs.logs_settint import mylogconfig
import logging

#импортируем настройки логирования
logging.basicConfig= mylogconfig

#определяем именные логеры
logging_get_exchange = logging.getLogger("get_exchange")
logging_get_stock_prices = logging.getLogger("get_stock_prices")

def get_exchange(currency):
    ''' Функция возвращает курс валюты которую подали в функцию относительно British Pound'''
    logging_get_exchange.info('Старт работы')
    load_dotenv()
    logging_get_exchange.info('Получили данные по API из дотенв')
    my_api =os.getenv("ApiKey_ninjas")
    currency_pair =currency+'_GBP'
    logging_get_exchange.info(f'Сформировали данные для направления запроса по АПИ {currency_pair}')

    api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair={currency_pair}'
    response = requests.get(api_url, headers={'X-Api-Key': my_api})
    if response.status_code == requests.codes.ok:
        logging_get_exchange.info('Данные по АПИ получены')
        return response.json()
    else:
        logging_get_exchange.error(f'Error:, {response.status_code}, {response.text}')
        return f'Error:, {response.status_code}, {response.text}'


def get_stock_prices(stock):
    logging_get_stock_prices.info('Запуск функции')
    load_dotenv()
    my_api = os.getenv("ApiKey_ninjas")
    logging_get_stock_prices.info('данные из dotenv получены')

    api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(stock)
    response = requests.get(api_url, headers={'X-Api-Key': my_api})
    if response.status_code == requests.codes.ok:
        logging_get_stock_prices.info('Данные по API получены успешно')
        return response.json()
    else:
        logging_get_stock_prices.info(f'Error:, {response.status_code}, {response.text}')
       return f'Error:, {response.status_code}, {response.text}'


