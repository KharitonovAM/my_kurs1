import json

from src.utill_web import take_filename_from_data
import pandas as pd
from src.setting import BASE_DIR
import re

def search_phone_number():
    '''Возвращает датафрейм, если в столбце описание содержится номер телефона
    в формате +Х ХХХ ХХХ-ХХ-ХХ'''

    exel_filename = take_filename_from_data()
    exel_dataframe = pd.read_excel(exel_filename)
    pattern = re.compile(r'\+\d \d{3} \d{3}-\d{2}-\d{2}')


    my_database = exel_dataframe[exel_dataframe['Описание'].str.contains(pattern)]
    json_file_with_phone_numbers = my_database.to_json(indent=4)

    return json_file_with_phone_numbers

