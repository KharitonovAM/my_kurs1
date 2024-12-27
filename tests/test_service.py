from src.services import search_phone_number


def test_search_phone_number(json_phone_rezult):
    """Тестируем что получая датафрейм с телефонными номерами, функция возвращает ожидаемые значения"""
    test_result = search_phone_number()
    assert test_result == json_phone_rezult
