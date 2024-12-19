import datetime
import os

def make_interval_dates(start_data:str, diap_data:str)->str:
    ''' Принимает дату и обозначение диапазона, возвращает стартовую дату'''

    data_object = datetime.datetime.strptime(start_data, '%d.%m.%Y')
    #обрабатываем когда подаётся W - начало интервала - понедельник текущей недели
    if diap_data.upper() == 'W':
        weekday_number = data_object.isoweekday()
        data_monday = data_object - datetime.timedelta(days= (weekday_number-1))
        return data_monday
    # обрабатываем когда подаётся M - начало интервала - первое число этого месяца
    elif diap_data.upper() == 'M':
        return data_object.replace(day=1)
    elif diap_data.upper() == 'Y':
        return data_object.replace(day=1, month=1)
    elif diap_data.upper() == 'ALL':
        return 'all_data'
    else:
        print('Ввели некорректные данные')
        raise ValueError


def take_filename_from_data():
    '''Функция возвращает название файла. который находится в директории data'''
    try:
        os.chdir('../data')
    except Exception:
        os.chdir('data')
    return os.listdir()[0]

