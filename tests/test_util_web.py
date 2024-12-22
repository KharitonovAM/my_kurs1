import pytest
from src.utill_web import make_list_dict_by_task, make_interval_dates, take_filename_from_data


def test_take_filename_from_data():
    assert take_filename_from_data() == 'operations.xlsx'

