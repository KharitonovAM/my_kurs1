import datetime

import pandas as pd
import pytest
from src.setting import excel_filename

from src.reports import spending_by_category, take_3_month_before


def test_spending_by_category_without_data(spending_without_data):
    '''Проверяем работу функции в случае если сумма трат по категории равна 0'''
    my_datafraim = pd.read_excel(excel_filename)
    assert spending_by_category(my_datafraim, "Переводы") == spending_without_data


def test_spending_by_category_with_data(spending_with_data):
    ''''Проверяем работу функции в случае если сумма трат по категории не равна 0'''
    my_datafraim = pd.read_excel(excel_filename)
    assert spending_by_category(my_datafraim, "Переводы", "18-12-2021 23:15:54") == spending_with_data


@pytest.mark.parametrize("start_data, result_data",
                         [(datetime.datetime(2020, 1, 1, 0, 0, 0), datetime.datetime(2019, 10, 1, 0, 0, 0),),
                          (datetime.datetime(2024, 10, 1, 0, 0, 0), datetime.datetime(2024, 7, 1, 0, 0, 0),), ], )
def test_take_3_month_before(start_data, result_data):
    '''Тестируем работу функции передавая разные значения временного объекта'''
    assert take_3_month_before(start_data) == result_data
