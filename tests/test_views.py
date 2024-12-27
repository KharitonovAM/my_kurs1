import json
import os
from unittest.mock import patch

import pytest

from src.views import events, main_page, take_data_from_json


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


def test_events_wrong_data(capsys):
    """Тестируем что при неправильных входных данных возникает ошибка"""
    events("11.10.24 17:10:10")
    captured = capsys.readouterr()
    assert captured.out == 'Возникла ошибка - проверьте logfile\nВозникла ошибка - проверьте logfile\n'


@patch("src.views.make_list_dict_from_json_data_stocks")
@patch("src.views.make_list_dict_from_json_data_currencies")
def test_events(stocks_mock, currencies_mock, capsys):
    """Тестируем функцию events что получив на вход корректные данные,
    возвращается результат в соответствии с ожиданиями"""
    stocks_mock.return_value = [{"FFP": 110}, {"RTR": 57}]
    currencies_mock.return_value = [{"eur": 110}, {"usd": 107}]
    events("2019-10-10 15:17:31")
    captured = capsys.readouterr()
    assert captured.out == ('{\n'
                            '    "expenses": {\n'
                            '        "total_amount": -91585.0,\n'
                            '        "main": [\n'
                            '            {\n'
                            '                "category": "Другое",\n'
                            '                "amount": 7195.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Супермаркеты",\n'
                            '                "amount": 3152.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Фастфуд",\n'
                            '                "amount": 2117.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Транспорт",\n'
                            '                "amount": 1286.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Ж/д билеты",\n'
                            '                "amount": 1114.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Одежда и обувь",\n'
                            '                "amount": 1077.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Связь",\n'
                            '                "amount": 500.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Остальное",\n'
                            '                "amount": 706.0\n'
                            '            }\n'
                            '        ],\n'
                            '        "transfers_and_cash": [\n'
                            '            {\n'
                            '                "category": "Переводы",\n'
                            '                "amount": 74437.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Наличные",\n'
                            '                "amount": 0\n'
                            '            }\n'
                            '        ]\n'
                            '    },\n'
                            '    "income": {\n'
                            '        "total_amount": 49885.0,\n'
                            '        "main": [\n'
                            '            {\n'
                            '                "category": "Пополнения",\n'
                            '                "amount": 24550.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Зарплата",\n'
                            '                "amount": 22200.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Переводы",\n'
                            '                "amount": 2635.0\n'
                            '            },\n'
                            '            {\n'
                            '                "category": "Бонусы",\n'
                            '                "amount": 500.0\n'
                            '            }\n'
                            '        ]\n'
                            '    },\n'
                            '    "currency_rates": [\n'
                            '        {\n'
                            '            "currency": "FFP",\n'
                            '            "rate": 110\n'
                            '        },\n'
                            '        {\n'
                            '            "currency": "RTR",\n'
                            '            "rate": 57\n'
                            '        }\n'
                            '    ],\n'
                            '    "stock_prices": [\n'
                            '        {\n'
                            '            "stock": "eur",\n'
                            '            "price": 110\n'
                            '        },\n'
                            '        {\n'
                            '            "stock": "usd",\n'
                            '            "price": 107\n'
                            '        }\n'
                            '    ]\n'
                            '}\n')


@patch("src.views.make_list_dict_from_json_data_stocks")
@patch("src.views.make_list_dict_from_json_data_currencies")
def test_main_page(stocks_mock, currencies_mock, capsys):
    """Тестируем функцию events что получив на вход корректные данные,
    возвращается результат в соответствии с ожиданиями"""
    stocks_mock.return_value = [{"FFP": 110}, {"RTR": 57}]
    currencies_mock.return_value = [{"eur": 110}, {"usd": 107}]
    main_page("2019-10-10 15:17:31")
    captured = capsys.readouterr()

    assert captured.out == (
        "{\n"
        '    "greeting": "Добрый день",\n'
        '    "cards": [\n'
        "        {\n"
        '            "last_digits": "4556",\n'
        '            "total_spent": 15805.23,\n'
        '            "cashback": "158.05"\n'
        "        },\n"
        "        {\n"
        '            "last_digits": "7197",\n'
        '            "total_spent": 1422.86,\n'
        '            "cashback": "14.23"\n'
        "        }\n"
        "    ],\n"
        '    "top_transactions": [\n'
        "        {\n"
        '            "date": "07.10.2019",\n'
        '            "amount": "50000.00",\n'
        '            "category": "Переводы",\n'
        '            "description": "На р/с ООО \\"ФОРТУНА\\""\n'
        "        },\n"
        "        {\n"
        '            "date": "08.10.2019",\n'
        '            "amount": "24000.00",\n'
        '            "category": "Переводы",\n'
        '            "description": "Иван С."\n'
        "        },\n"
        "        {\n"
        '            "date": "01.10.2019",\n'
        '            "amount": "22200.00",\n'
        '            "category": "Зарплата",\n'
        '            "description": "Пополнение. ООО \\"ФОРТУНА\\". Зарплата"\n'
        "        },\n"
        "        {\n"
        '            "date": "02.10.2019",\n'
        '            "amount": "14550.00",\n'
        '            "category": "Пополнения",\n'
        '            "description": "Перевод с карты"\n'
        "        },\n"
        "        {\n"
        '            "date": "06.10.2019",\n'
        '            "amount": "10000.00",\n'
        '            "category": "Пополнения",\n'
        '            "description": "Перевод с карты"\n'
        "        }\n"
        "    ],\n"
        '    "currency_rates": [\n'
        "        {\n"
        '            "currency": "FFP",\n'
        '            "rate": 110\n'
        "        },\n"
        "        {\n"
        '            "currency": "RTR",\n'
        '            "rate": 57\n'
        "        }\n"
        "    ],\n"
        '    "stock_prices": [\n'
        "        {\n"
        '            "stock": "eur",\n'
        '            "price": 110\n'
        "        },\n"
        "        {\n"
        '            "stock": "usd",\n'
        '            "price": 107\n'
        "        }\n"
        "    ]\n"
        "}\n"
    )
