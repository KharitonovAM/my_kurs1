import pandas as pd
import pytest


@pytest.fixture
def spending_without_data():
    return 0.0


@pytest.fixture
def spending_with_data():
    return -35049.92


@pytest.fixture
def list_of_data_result():
    return ["2012-11-01 23:54:16", "M", "2012-11-01 00:00:00"]


@pytest.fixture
def return_dict():
    return """   "expenses": {
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
"""


@pytest.fixture
def json_phone_rezult():
    return """{
    "Дата операции": {
        "259": "18.11.2021 21:15:27",
        "260": "18.11.2021 21:15:27",
        "1572": "14.03.2021 09:49:03",
        "1616": "07.03.2021 12:00:06",
        "1690": "19.02.2021 19:37:03",
        "1886": "28.12.2020 10:01:58",
        "1990": "03.12.2020 23:32:21",
        "2013": "29.11.2020 09:29:33",
        "2034": "25.11.2020 18:11:15",
        "2112": "10.11.2020 23:31:41",
        "2132": "05.11.2020 19:19:14",
        "2138": "04.11.2020 23:05:37",
        "2167": "28.10.2020 12:35:11",
        "2559": "22.07.2020 10:19:29",
        "2565": "18.07.2020 21:05:23",
        "2942": "18.03.2020 17:28:04",
        "3551": "05.11.2019 09:40:44",
        "3552": "05.11.2019 09:38:52",
        "5002": "31.01.2019 13:34:15",
        "5296": "18.11.2018 14:46:44",
        "5307": "14.11.2018 20:43:00",
        "5465": "18.10.2018 17:01:08",
        "5466": "18.10.2018 17:00:25",
        "5975": "03.07.2018 21:30:39",
        "6309": "12.04.2018 11:03:57"
    },
    "Дата платежа": {
        "259": "19.11.2021",
        "260": "19.11.2021",
        "1572": "14.03.2021",
        "1616": "07.03.2021",
        "1690": "19.02.2021",
        "1886": "28.12.2020",
        "1990": "04.12.2020",
        "2013": "29.11.2020",
        "2034": "25.11.2020",
        "2112": "11.11.2020",
        "2132": "05.11.2020",
        "2138": "05.11.2020",
        "2167": "28.10.2020",
        "2559": "22.07.2020",
        "2565": "19.07.2020",
        "2942": "18.03.2020",
        "3551": "05.11.2019",
        "3552": "05.11.2019",
        "5002": "31.01.2019",
        "5296": "18.11.2018",
        "5307": "14.11.2018",
        "5465": "18.10.2018",
        "5466": "18.10.2018",
        "5975": "03.07.2018",
        "6309": "12.04.2018"
    },
    "Номер карты": {
        "259": NaN,
        "260": NaN,
        "1572": NaN,
        "1616": NaN,
        "1690": NaN,
        "1886": NaN,
        "1990": NaN,
        "2013": NaN,
        "2034": NaN,
        "2112": NaN,
        "2132": NaN,
        "2138": NaN,
        "2167": NaN,
        "2559": NaN,
        "2565": NaN,
        "2942": NaN,
        "3551": NaN,
        "3552": NaN,
        "5002": NaN,
        "5296": NaN,
        "5307": NaN,
        "5465": NaN,
        "5466": NaN,
        "5975": NaN,
        "6309": NaN
    },
    "Статус": {
        "259": "OK",
        "260": "OK",
        "1572": "OK",
        "1616": "OK",
        "1690": "OK",
        "1886": "OK",
        "1990": "OK",
        "2013": "OK",
        "2034": "OK",
        "2112": "OK",
        "2132": "OK",
        "2138": "OK",
        "2167": "OK",
        "2559": "OK",
        "2565": "OK",
        "2942": "OK",
        "3551": "OK",
        "3552": "OK",
        "5002": "OK",
        "5296": "OK",
        "5307": "OK",
        "5465": "OK",
        "5466": "OK",
        "5975": "OK",
        "6309": "OK"
    },
    "Сумма операции": {
        "259": -200.0,
        "260": 200.0,
        "1572": -150.0,
        "1616": -50.0,
        "1690": -20.0,
        "1886": -100.0,
        "1990": -10.0,
        "2013": -300.0,
        "2034": -200.0,
        "2112": -100.0,
        "2132": -10.0,
        "2138": -50.0,
        "2167": -100.0,
        "2559": -100.0,
        "2565": -50.0,
        "2942": -400.0,
        "3551": -50.0,
        "3552": -500.0,
        "5002": -35.0,
        "5296": -200.0,
        "5307": -150.0,
        "5465": -40.0,
        "5466": -40.0,
        "5975": -150.0,
        "6309": -300.0
    },
    "Валюта операции": {
        "259": "RUB",
        "260": "RUB",
        "1572": "RUB",
        "1616": "RUB",
        "1690": "RUB",
        "1886": "RUB",
        "1990": "RUB",
        "2013": "RUB",
        "2034": "RUB",
        "2112": "RUB",
        "2132": "RUB",
        "2138": "RUB",
        "2167": "RUB",
        "2559": "RUB",
        "2565": "RUB",
        "2942": "RUB",
        "3551": "RUB",
        "3552": "RUB",
        "5002": "RUB",
        "5296": "RUB",
        "5307": "RUB",
        "5465": "RUB",
        "5466": "RUB",
        "5975": "RUB",
        "6309": "RUB"
    },
    "Сумма платежа": {
        "259": -200.0,
        "260": 200.0,
        "1572": -150.0,
        "1616": -50.0,
        "1690": -20.0,
        "1886": -100.0,
        "1990": -10.0,
        "2013": -300.0,
        "2034": -200.0,
        "2112": -100.0,
        "2132": -10.0,
        "2138": -50.0,
        "2167": -100.0,
        "2559": -100.0,
        "2565": -50.0,
        "2942": -400.0,
        "3551": -50.0,
        "3552": -500.0,
        "5002": -35.0,
        "5296": -200.0,
        "5307": -150.0,
        "5465": -40.0,
        "5466": -40.0,
        "5975": -150.0,
        "6309": -300.0
    },
    "Валюта платежа": {
        "259": "RUB",
        "260": "RUB",
        "1572": "RUB",
        "1616": "RUB",
        "1690": "RUB",
        "1886": "RUB",
        "1990": "RUB",
        "2013": "RUB",
        "2034": "RUB",
        "2112": "RUB",
        "2132": "RUB",
        "2138": "RUB",
        "2167": "RUB",
        "2559": "RUB",
        "2565": "RUB",
        "2942": "RUB",
        "3551": "RUB",
        "3552": "RUB",
        "5002": "RUB",
        "5296": "RUB",
        "5307": "RUB",
        "5465": "RUB",
        "5466": "RUB",
        "5975": "RUB",
        "6309": "RUB"
    },
    "Кэшбэк": {
        "259": NaN,
        "260": NaN,
        "1572": NaN,
        "1616": NaN,
        "1690": NaN,
        "1886": NaN,
        "1990": NaN,
        "2013": NaN,
        "2034": NaN,
        "2112": NaN,
        "2132": NaN,
        "2138": NaN,
        "2167": NaN,
        "2559": NaN,
        "2565": NaN,
        "2942": NaN,
        "3551": NaN,
        "3552": NaN,
        "5002": NaN,
        "5296": NaN,
        "5307": NaN,
        "5465": NaN,
        "5466": NaN,
        "5975": NaN,
        "6309": NaN
    },
    "Категория": {
        "259": "Мобильная связь",
        "260": "Пополнения",
        "1572": "Мобильная связь",
        "1616": "Мобильная связь",
        "1690": "Мобильная связь",
        "1886": "Мобильная связь",
        "1990": "Мобильная связь",
        "2013": "Мобильная связь",
        "2034": "Мобильная связь",
        "2112": "Мобильная связь",
        "2132": "Мобильная связь",
        "2138": "Мобильная связь",
        "2167": "Мобильная связь",
        "2559": "Мобильная связь",
        "2565": "Мобильная связь",
        "2942": "Мобильная связь",
        "3551": "Мобильная связь",
        "3552": "Мобильная связь",
        "5002": "Мобильная связь",
        "5296": "Мобильная связь",
        "5307": "Мобильная связь",
        "5465": "Мобильная связь",
        "5466": "Мобильная связь",
        "5975": "Мобильная связь",
        "6309": "Мобильная связь"
    },
    "MCC": {
        "259": NaN,
        "260": NaN,
        "1572": NaN,
        "1616": NaN,
        "1690": NaN,
        "1886": NaN,
        "1990": NaN,
        "2013": NaN,
        "2034": NaN,
        "2112": NaN,
        "2132": NaN,
        "2138": NaN,
        "2167": NaN,
        "2559": NaN,
        "2565": NaN,
        "2942": NaN,
        "3551": NaN,
        "3552": NaN,
        "5002": NaN,
        "5296": NaN,
        "5307": NaN,
        "5465": NaN,
        "5466": NaN,
        "5975": NaN,
        "6309": NaN
    },
    "Описание": {
        "259": "Тинькофф Мобайл +7 995 555-55-55",
        "260": "Тинькофф Мобайл +7 995 555-55-55",
        "1572": "МТС Mobile +7 981 333-44-55",
        "1616": "МТС Mobile +7 981 333-33-33",
        "1690": "МегаФон +7 921 333-33-33",
        "1886": "МТС Mobile +7 921 111-22-33",
        "1990": "МТС +7 981 666-66-66",
        "2013": "МТС Mobile +7 921 111-22-33",
        "2034": "МТС Mobile +7 981 888-88-88",
        "2112": "МТС +7 981 976-14-20",
        "2132": "МТС +7 981 976-14-20",
        "2138": "МТС +7 981 976-14-20",
        "2167": "Я МТС +7 921 111-22-33",
        "2559": "МТС Mobile +7 985 111-11-11",
        "2565": "МТС Mobile +7 921 999-99-99",
        "2942": "МТС +7 911 198-78-58",
        "3551": "МТС +7 981 555-55-55",
        "3552": "МТС +7 981 976-14-20",
        "5002": "Teletie Бизнес +7 966 000-00-00",
        "5296": "МТС +7 911 000-09-09",
        "5307": "МТС +7 911 882-65-08",
        "5465": "Билайн +7 962 717-08-52",
        "5466": "Билайн +7 962 717-08-52",
        "5975": "МТС +7 981 127-94-00",
        "6309": "МТС +7 911 695-42-03"
    },
    "Бонусы (включая кэшбэк)": {
        "259": 2,
        "260": 0,
        "1572": 0,
        "1616": 0,
        "1690": 0,
        "1886": 0,
        "1990": 0,
        "2013": 0,
        "2034": 0,
        "2112": 0,
        "2132": 0,
        "2138": 0,
        "2167": 1,
        "2559": 0,
        "2565": 0,
        "2942": 0,
        "3551": 0,
        "3552": 0,
        "5002": 0,
        "5296": 2,
        "5307": 1,
        "5465": 0,
        "5466": 0,
        "5975": 1,
        "6309": 3
    },
    "Округление на инвесткопилку": {
        "259": 0,
        "260": 0,
        "1572": 0,
        "1616": 0,
        "1690": 0,
        "1886": 0,
        "1990": 0,
        "2013": 0,
        "2034": 0,
        "2112": 0,
        "2132": 0,
        "2138": 0,
        "2167": 0,
        "2559": 0,
        "2565": 0,
        "2942": 0,
        "3551": 0,
        "3552": 0,
        "5002": 0,
        "5296": 0,
        "5307": 0,
        "5465": 0,
        "5466": 0,
        "5975": 0,
        "6309": 0
    },
    "Сумма операции с округлением": {
        "259": 200.0,
        "260": 200.0,
        "1572": 150.0,
        "1616": 50.0,
        "1690": 20.0,
        "1886": 100.0,
        "1990": 10.0,
        "2013": 300.0,
        "2034": 200.0,
        "2112": 100.0,
        "2132": 10.0,
        "2138": 50.0,
        "2167": 100.0,
        "2559": 100.0,
        "2565": 50.0,
        "2942": 400.0,
        "3551": 50.0,
        "3552": 500.0,
        "5002": 35.0,
        "5296": 200.0,
        "5307": 150.0,
        "5465": 40.0,
        "5466": 40.0,
        "5975": 150.0,
        "6309": 300.0
    }
}"""


@pytest.fixture
def my_dataset():
    my_dataset = {
        "Номер карты": ["*4321", " ", "*2251", "*4321"],
        "Сумма платежа": [28, 34, 29, 121],
    }
    return pd.DataFrame(my_dataset)
