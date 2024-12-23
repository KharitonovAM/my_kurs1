import pytest
from unittest.mock import patch
import pandas as pd

import src.utill_web
from src.services import search_phone_number
from src.utill_web import take_filename_from_data



def test_search_phone_number(json_phone_rezult):
    test_result = search_phone_number()
    assert test_result == json_phone_rezult
