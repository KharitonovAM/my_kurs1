from unittest.mock import patch


from src.api_utils import get_exchange, get_stock_prices


@patch("requests.get")
def test_get_exchange(mock_get):
    "Тестируем функционал получение данных по курсу GBP_EUR"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "currency_pair": "GBP_EUR",
        "exchange_rate": 1.911863,
    }
    assert get_exchange("AUD") == {
        "currency_pair": "GBP_EUR",
        "exchange_rate": 1.911863,
    }


@patch("requests.get")
def test_get_stock_prices(mock_get):
    "Тестируем функционал получения данных по стоимости акций через API"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "ticker": "AAPL",
        "name": "Apple Inc.",
        "price": 192.42,
        "exchange": "NASDAQ",
        "updated": 1706302801,
        "currency": "USD",
    }
    assert get_stock_prices("AAPL") == {
        "ticker": "AAPL",
        "name": "Apple Inc.",
        "price": 192.42,
        "exchange": "NASDAQ",
        "updated": 1706302801,
        "currency": "USD",
    }


@patch("requests.get")
def test_get_exchange_bad_data(get_mock):
    """Тестируем функционал по возвращению ошибки"""
    get_mock.return_value.status_code = 400
    get_mock.return_value.text = "This currency pair is for premium subscribers only"
    assert get_exchange("rere") == "Error:, 400, This currency pair is for premium subscribers only"


@patch("requests.get")
def test_get_stock_prices_bad_data(get_mock):
    """Тестируем функционал по возвращению данных в случае возбуждения ошибки"""
    get_mock.return_value.status_code = 400
    get_mock.return_value.text = "This company hasn't stock"
    assert get_exchange("skypro") == "Error:, 400, This company hasn't stock"
