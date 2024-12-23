from src.utill_web import take_filename_from_data
import pandas as pd
import re

def search_phone_number():
    '''Возвращает датафрейм, если в столбце описание содержится номер телефона
    в формате +Х ХХХ ХХХ-ХХ-ХХ'''

    #Получаем данные из эксель-файла
    exel_filename = take_filename_from_data()
    exel_dataframe = pd.read_excel(exel_filename)
    # Объявляем паттерн
    pattern = re.compile(r'\+\d \d{3} \d{3}-\d{2}-\d{2}')
    # Формируем датафрейм из строк в которых в описании есть совпадение по паттерну
    my_database = exel_dataframe[exel_dataframe['Описание'].str.contains(pattern)]
    # Сохраняем датабейс в формате json
    json_file_with_phone_numbers = my_database.to_json(indent=4)

    return json_file_with_phone_numbers

