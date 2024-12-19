from typing import Any
import json
from src.views import take_filename_from_data


def main(data:str, diapazon_dates:str='M')->dict[Any,Any]:

    '''принимающую на вход строку с датой и второй необязательный параметр — диапазон данных.
    По умолчанию диапазон равен одному месяцу (с начала месяца, на который выпадает дата, по саму дату).
    Возвращаемый JSON-ответ содержит следующие данные:
    Расходы
    Поступления
    Курс валют
    Стоимость акций из S&P 500
    '''
    pass






if __name__ == '__main__':
    take_filename_from_data()
    pass
