from src.services import search_phone_number


def test_search_phone_number(json_phone_rezult):
    test_result = search_phone_number()
    assert test_result == json_phone_rezult
