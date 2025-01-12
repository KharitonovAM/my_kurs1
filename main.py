from src.views import events


def main(data: str, diapazon_dates: str = 'M') -> None:
    '''принимающую на вход строку с датой и второй необязательный параметр — диапазон данных.
    По умолчанию диапазон равен одному месяцу (с начала месяца, на который выпадает дата, по саму дату).
    Возвращаемый JSON-ответ содержит следующие данные:
    Расходы
    Поступления
    Курс валют
    Стоимость акций из S&P 500
    '''

    events(data, diapazon_dates)


if __name__ == '__main__':
    main('2019-11-15 10:01:15', 'Y')
