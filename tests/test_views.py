import json
import os
from unittest.mock import patch

import pytest

from src.views import (events,
                       take_data_from_json)


def test_take_data_from_json():
    """Тестируем получение данных из файла, который создаем во время теста"""
    with open("temp_file", "w") as f:
        json.dump({"user_currencies": 100, "user_stocks": 200}, f)
    assetr_return = take_data_from_json("temp_file")
    os.remove("temp_file")
    assert assetr_return == (100, 200)


def test_mistake_take_data_from_json():
    """Проверяем возбуждение ошибки в случае неверного наименвоание файла"""
    with pytest.raises(TypeError):
        assert test_take_data_from_json("no_such_file.txt")


def test_events_wrong_data():
    """Тестируем что при неправильных входных данных возникает ошибка"""
    with pytest.raises(ValueError):
        events("11.10.24 17:10:10")


@patch("src.views.make_list_dict_from_json_data_stocks")
@patch("src.views.make_list_dict_from_json_data_currencies")
def test_events(stocks_mock, currencies_mock):
    stocks_mock.return_value = [{"FFP": 110}, {"RTR": 57}]
    currencies_mock.return_value = [{"eur": 110}, {"usd": 107}]
    assert events("2019-10-10 15:17:31") == None


