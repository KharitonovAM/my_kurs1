import pytest
import pandas as pd
import datetime
from src.reports import spending_by_category, take_3_month_before


def test_spending_by_category_without_data(spending_without_data):
    my_datafraim = pd.read_excel(
        'G:\Учеба скай про\курсовые работы\Курсовая работа 1\pythonProject\data\operations.xlsx')
    assert spending_by_category(my_datafraim, 'Переводы') == spending_without_data


def test_spending_by_category_with_data(spending_with_data):
    my_datafraim = pd.read_excel(
        'G:\Учеба скай про\курсовые работы\Курсовая работа 1\pythonProject\data\operations.xlsx')
    assert spending_by_category(my_datafraim, 'Переводы', '18-12-2021 23:15:54') == spending_with_data


@pytest.mark.parametrize('start_data, result_data',[(datetime.datetime(2020, 1, 1, 0, 0, 0),
                                                     datetime.datetime(2019, 10, 1, 0, 0, 0)),
                                                    (datetime.datetime(2024, 10, 1, 0, 0, 0),
                                                     datetime.datetime(2024, 7, 1, 0, 0, 0))])
def test_take_3_month_before(start_data, result_data):
    assert take_3_month_before(start_data) == result_data
