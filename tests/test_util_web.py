import pytest
from freezegun import freeze_time

from src.utill_web import (make_interval_dates, make_list_dict_by_task,
                           take_filename_from_data, web_meeting)


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
    assert str(make_interval_dates(start_data, interval)) == result_data


def test_make_interval_dates_value_error():
    with pytest.raises(ValueError):
        assert make_interval_dates("2012-11-01 23:54:16", "N")

@freeze_time('2012-11-01 08:08:00')
def test_web_meeting_morning():
    assert web_meeting() == 'Доброе утро'


@freeze_time('2012-11-01 12:08:00')
def test_web_meeting_day():
    assert web_meeting() == 'Добрый день'


@freeze_time('2012-11-01 19:08:00')
def test_web_meeting_day():
    assert web_meeting() == 'Добрый вечер'


@freeze_time('2012-11-01 23:08:00')
def test_web_meeting_day():
    assert web_meeting() == 'Доброй ночи'