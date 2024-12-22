import pytest

@pytest.fixture
def list_of_data_result():
    return ['2012-11-01 23:54:16','M', '2012-11-01 00:00:00']

@pytest.fixture
def return_dict():
    return '''   "expenses": {
        "total_amount": -91584.76000000001,
        "main": [
            {
                "category": "Другое",
                "amount": 7194.76
            },
            {
                "category": "Супермаркеты",
                "amount": 3152.5
            },
            {
                "category": "Фастфуд",
                "amount": 2116.9700000000003
            },
            {
                "category": "Транспорт",
                "amount": 1286.43
            },
            {
                "category": "Ж/д билеты",
                "amount": 1114.4299999999998
            },
            {
                "category": "Одежда и обувь",
                "amount": 1077.0
            },
            {
                "category": "Связь",
                "amount": 500.0
            },
            {
                "category": "Остальное",
                "amount": 706.0
            }
        ],
        "transfers_and_cash": [
            {
                "category": "Переводы",
                "amount": 74436.67
            },
            {
                "category": "Наличные",
                "amount": 0
            }
        ]
    },
    "income": {
        "total_amount": 49884.86,
        "main": [
            {
                "category": "Пополнения",
                "amount": 24550.0
            },
            {
                "category": "Зарплата",
                "amount": 22200.0
            },
            {
                "category": "Переводы",
                "amount": 2634.86
            },
            {
                "category": "Бонусы",
                "amount": 500.0
            }
        ]
    },
    "currency_rates": [
        {
            "currency": "FFP",
            "rate": 110
        },
        {
            "currency": "RTR",
            "rate": 57
        }
    ],
    "stock_prices": [
        {
            "stock": "eur",
            "price": 110
        },
        {
            "stock": "usd",
            "price": 107
        }
    ]
}
'''