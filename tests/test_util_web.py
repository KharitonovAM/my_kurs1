import pytest
from src.utill_web import make_list_dict_by_task, make_interval_dates, take_filename_from_data


def test_take_filename_from_data():
    '''Тестирует. что возвращается корректное наименование файла'''
    assert take_filename_from_data() == 'operations.xlsx'


def test_make_list_dict_by_task():
    assert make_list_dict_by_task([{1:'one'}, {2: 'two'}],'цифра','слово') == [{'цифра': 1, 'слово': 'one'}, {'цифра': 2, 'слово': 'two'}]

