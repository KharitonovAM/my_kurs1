import datetime
import logging
import os

from logs.logs_settint import mylogconfig

# импортируем настройки логирования
logging.basicConfig = mylogconfig

# определяем именные логеры
logging_make_interval_dates = logging.getLogger("make_interval_dates")
logging_take_filename_from_data = logging.getLogger("take_filename_from_data")
logging_make_list_dict_by_task = logging.getLogger("make_list_dict_by_task")
logging_web_meeting = logging.getLogger('logging_web_meeting')


def make_interval_dates(start_data: str, diap_data: str) -> str:
    """Принимает дату и обозначение диапазона, возвращает стартовую дату"""

    logging_make_interval_dates.info("Запустили программу")
    data_object = datetime.datetime.strptime(start_data, "%Y-%m-%d %H:%M:%S")
    # обрабатываем когда подаётся W - начало интервала - понедельник текущей недели
    if diap_data.upper() == "W":
        weekday_number = data_object.isoweekday()
        data_monday = data_object - datetime.timedelta(days=(weekday_number - 1))
        return data_monday.replace(hour=0, minute=0, second=0)
    # обрабатываем когда подаётся M - начало интервала - первое число этого месяца
    elif diap_data.upper() == "M":
        return data_object.replace(day=1, hour=0, minute=0, second=0)
    elif diap_data.upper() == "Y":
        return data_object.replace(day=1, month=1, hour=0, minute=0, second=0)
    elif diap_data.upper() == "ALL":
        logging_make_interval_dates.info("Программа отработала штатно")
        return "all_data"
    else:
        logging_make_interval_dates.error("Введены некорректные данные")
        print("Ввели некорректные данные")
        raise ValueError


def take_filename_from_data():
    """Функция возвращает название файла. который находится в директории data"""
    logging_take_filename_from_data.info("Запуск программы")
    try:
        os.chdir("../data")
    except Exception:
        os.chdir("data")
    logging_take_filename_from_data.info("Отработала штатно")
    return os.listdir()[0]


def make_list_dict_by_task(list_dict, first_category, second_category):
    """Принимает на вход список словарей, и названия двух категорий,
    которые будут слуужить ключами для новых словарей, список которых вернёт функция,
    чтобы вывод соответствовал заданному в ТЗ"""
    logging_make_list_dict_by_task.info("Запустили программу")
    result_list = []
    for item in list_dict:
        result_dict = {}
        for k, v in item.items():
            result_dict[first_category] = k
            result_dict[second_category] = v
        result_list.append(result_dict)
    logging_make_list_dict_by_task.info("Отработала штатно")
    return result_list



def web_meeting():
    '''Генерирует приветствие в зависимости от текущего времени суток: утро, день, вечер '''
    logging_web_meeting.info('Старт работы программы')
    #Получаем текущее время
    the_time = datetime.datetime.now()
    logging_web_meeting.info(f'На старте программы время {the_time}')
    #В зависимости от значения часа возвращаем приветствие
    if 6 <= the_time.hour and the_time.hour <= 10:
        logging_web_meeting.info('Доброе утро')
        return 'Доброе утро'
    elif the_time.hour <= 17:
        logging_web_meeting.info('Добрый день')
        return 'Добрый день'
    elif the_time.hour <= 21:
        logging_web_meeting.info('Добрый вечер')
        return 'Добрый вечер'
    else:
        logging_web_meeting.info('Доброй ночи')
        return 'Доброй ночи'
