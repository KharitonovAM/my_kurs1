import pytest
from freezegun import freeze_time

from src.utill_web import (make_interval_dates, make_list_dict_by_task,
                           take_filename_from_data,
                           take_list_with_for_last_number_cards, web_meeting)


def test_take_filename_from_data():
    """Тестирует. что возвращается корректное наименование файла"""
    assert take_filename_from_data() == "operations.xlsx"


def test_make_list_dict_by_task():
    """Тестируем на корректную работу функции по формированию словаря согласно ТЗ"""
    assert make_list_dict_by_task([{1: "one"}, {2: "two"}], "цифра", "слово") == [
        {"цифра": 1, "слово": "one"},
        {"цифра": 2, "слово": "two"},
    ]


@pytest.mark.parametrize(
    "start_data, interval, result_data",
    [
        ("2012-11-01 23:54:16", "M", "2012-11-01 00:00:00"),
        ("2012-11-01 23:54:16", "W", "2012-10-29 00:00:00"),
        ("2012-11-01 23:54:16", "Y", "2012-01-01 00:00:00"),
        ("2012-11-01 23:54:16", "ALL", "all_data"),
    ],
)
def test_make_interval_dates(start_data, interval, result_data):
    '''Тестируем make_interval_dates: передаем стартовые данные, интервал,
    полученный результат соответствует ожиданиям'''
    assert str(make_interval_dates(start_data, interval)) == result_data


def test_make_interval_dates_value_error():
    '''Тестируем make_interval_dates: передаем стартовые данные, некоректный интервал,
    в результате возбуждается исключение'''
    with pytest.raises(ValueError):
        assert make_interval_dates("2012-11-01 23:54:16", "N")

@freeze_time('2012-11-01 08:08:00')
def test_web_meeting_morning():
    '''Тестируем web_meeting_morning, что получчив данные утреннего времении,
    возвращаем Доброе утро'''
    assert web_meeting() == 'Доброе утро'


@freeze_time('2012-11-01 12:08:00')
def test_web_meeting_day():
    '''Тестируем web_meeting_morning, что получчив данные дневного времении,
    возвращаем Добрый день'''
    assert web_meeting() == 'Добрый день'


@freeze_time('2012-11-01 19:08:00')
def test_web_meeting_evening():
    '''Тестируем web_meeting_morning, что получчив данные вечернего времении,
    возвращаем Добрый вечер'''
    assert web_meeting() == 'Добрый вечер'


@freeze_time('2012-11-01 23:08:00')
def test_web_meeting_night():
    '''Тестируем web_meeting_morning, что получчив данные ночного времении,
    возвращаем Доброй ночи'''
    assert web_meeting() == 'Доброй ночи'


def test_take_list_with_for_last_number_cards(my_dataset):
    '''Тестируем wtake_list_with_for_last_number_cards,
    что получив корректные данные получаем результат в соответствии с ожиданиями'''
    assert take_list_with_for_last_number_cards(my_dataset, 'Номер карты') == ['2251', '4321']

def test_take_list_with_for_last_number_cards_with_mist():
    '''Тестируем wtake_list_with_for_last_number_cards,
    что в случае отсутствия датафрейма возбуждается исключение'''
    with pytest.raises(TypeError):
        assert take_list_with_for_last_number_cards()
