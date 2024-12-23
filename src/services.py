import json

from src.utill_web import take_filename_from_data
import pandas as pd
import re
from logs.logs_settint import mylogconfig
import logging

#импортируем настройки логирования
logging.basicConfig = mylogconfig

#определяем именные логеры
logging_search_phone_number = logging.getLogger("search_phone_number")

def search_phone_number():
    '''Возвращает датафрейм, если в столбце описание содержится номер телефона
    в формате +Х ХХХ ХХХ-ХХ-ХХ'''

    logging_search_phone_number.info('Запуск функции')
    #Получаем данные из эксель-файла
    exel_filename = take_filename_from_data()
    exel_dataframe = pd.read_excel(exel_filename)
    logging_search_phone_number.info(f'Получили данные из {exel_dataframe}')
    # Объявляем паттерн
    pattern = re.compile(r'\+\d \d{3} \d{3}-\d{2}-\d{2}')
    # Формируем датафрейм из строк в которых в описании есть совпадение по паттерну
    my_database = exel_dataframe[exel_dataframe['Описание'].str.contains(pattern)]
    logging_search_phone_number.info('Сформиировал датафрейм отфильрованные по номерамм телефона')
    # Сохраняем датабейс в формате словаря
    dict_file_with_phone_numbers = my_database.to_dict()
    #Переводим словарь json
    json_file_with_phone_numbers = json.dumps(dict_file_with_phone_numbers, indent=4, ensure_ascii=False)
    logging_search_phone_number.info('Функция отработала. сформирован json')
    return json_file_with_phone_numbers
