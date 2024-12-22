import pytest
import os
import json
from src.views import (events,
                       get_data_from_exel,
                       take_data_from_json,
                       make_list_dict_from_json_data_currencies,
                       make_list_dict_from_json_data_stocks)

def test_take_data_from_json():
    '''Тестируем получение данных из файла, который создаем во время теста'''
    with open('temp_file','w') as f:
        json.dump({"user_currencies":100, "user_stocks":200}, f)
    assetr_return = take_data_from_json('temp_file')
    os.remove('temp_file')
    assert assetr_return == (100, 200)


def test_mistake_take_data_from_json():
    '''Проверяем возбуждение ошибки в случае неверного наименвоание файла'''
    with pytest.raises(TypeError):
        assert test_take_data_from_json('no_such_file.txt')


