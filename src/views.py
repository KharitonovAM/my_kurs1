import json
import logging
from pathlib import Path

import pandas as pd

from logs.logs_settint import mylogconfig
from src.api_utils import get_exchange, get_stock_prices
from src.setting import BASE_DIR
from src.utill_web import (make_interval_dates, make_list_dict_by_task,
                           take_filename_from_data)

# импортируем настройки логирования
logging.basicConfig = mylogconfig

# определяем именные логеры
logging_get_data_from_exel = logging.getLogger("get_data_from_exel")
logging_take_data_from_json = logging.getLogger("take_data_from_json")
logging_make_list_dict_from_json_data_currencies = logging.getLogger(
    "make_list_dict_from_json_data_currencies"
)
logging_make_list_dict_from_json_data_stocks = logging.getLogger(
    "make_list_dict_from_json_data_stocks"
)
logging_events = logging.getLogger("events")


def get_data_from_exel(filename, type_of_operation, start_data, diap_data):
    """Функция получает на вход имя файла и тип операции 0 -
    если нужна информация о расходах, 1 - если нужна информация о доходах"""

    logging_get_data_from_exel.info("Старт работы")
    # Формируем предварительно рабочий датафрейм (без учета временного интервала)
    exel_dataframe = pd.read_excel(filename)
    only_real_operations = exel_dataframe[exel_dataframe["Статус"] == "OK"]
    only_real_operations["Дата операции"] = pd.to_datetime(
        only_real_operations["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )
    logging_get_data_from_exel.info(
        f"Сформировали датафрейм из информации файла {filename} согласно ТЗ"
    )

    # получаем интервал дат, в рамках которых будет формировать рабочий датафрейм:
    start_data_interval = make_interval_dates(start_data, diap_data)

    # формируем промежуточный рабочий датафрейм с учетом временных интервалов
    if start_data_interval != "all_data":
        only_real_operations = only_real_operations[
            only_real_operations["Дата операции"] >= start_data_interval
        ]
        only_real_operations = only_real_operations[
            only_real_operations["Дата операции"] <= start_data
        ]
    logging_get_data_from_exel.info(
        f"Сформировали датафрейм с учетом данных по времени {start_data_interval}"
    )

    # формируем датафрейм с учтом того, нужны нам данные по расходам или по доходам
    if type_of_operation == 0:
        dataframe_for_work = only_real_operations[
            only_real_operations["Сумма платежа"] < 0
        ]
    else:
        dataframe_for_work = only_real_operations[
            only_real_operations["Сумма платежа"] > 0
        ]
    logging_get_data_from_exel.info("Сформировали датафрейм доходы/расходы")

    # получаем общую сумму по операциям в рабочем датафрейме
    total_summ = round(dataframe_for_work["Сумма платежа"].sum(), 0)

    # получаем список с перечнем категорий
    list_of_categories = list(set(dataframe_for_work["Категория"]))

    # формируем список со словарями категория: сумма по категории
    return_list = []
    for item in list_of_categories:
        z = {}
        z[item] = round(
            abs(
                float(
                    dataframe_for_work[dataframe_for_work["Категория"] == item][
                        "Сумма платежа"
                    ].sum()
                )
            ),
            0,
        )
        return_list.append(z)

    # сортируем список по убыванию суммы по категориям
    return_list = sorted(return_list, key=lambda x: list(x.values())[0], reverse=True)
    logging_get_data_from_exel.info(
        "Сформировали список категорий отфильтрованный по убыванию"
    )

    # формируем список с данными по расходу наличных выводя их в отдельный список
    if type_of_operation == 0:
        cash_list = [{"Наличные": 0}, {"Переводы": 0}]
        for item in return_list:
            if list(item.keys())[0] == "Наличные":
                cash_list[0]["Наличные"] = list(item.values())[0]
                return_list.remove(item)
            elif list(item.keys())[0] == "Переводы":
                cash_list[1]["Переводы"] = list(item.values())[0]
                return_list.remove(item)

        # сртируем список наличных по убыванию
        cash_list = sorted(cash_list, key=lambda x: list(x.values())[0], reverse=True)
        logging_get_data_from_exel.info(
            "Сформировали список наличных отфильтрованный по убыванию"
        )

        # Преобразовываем список с категориями, оставляя 7 категорий и остальное
        if len(return_list) > 7:
            summ_other = round(sum([list(x.values())[0] for x in return_list[7:]]), 0)
            return_list = return_list[:7] + [{"Остальное": summ_other}]
            logging_get_data_from_exel.info(
                "Получили сумму категорий которые попадуьт в остальное"
            )

        logging_get_data_from_exel.info("Программа успешно отработала")
        return cash_list, return_list, total_summ
    logging_get_data_from_exel.info("Программа успешно отработала")
    return return_list, total_summ


def take_data_from_json(filename=Path(BASE_DIR, "user_settings.json")):
    """Получает данные из json файла"""
    logging_take_data_from_json.info("Старт программы")
    with open(filename, "r") as f:
        my_data = json.load(f)
    logging_take_data_from_json.info("Программа успешно отработала")
    return my_data["user_currencies"], my_data["user_stocks"]


def make_list_dict_from_json_data_currencies(list):
    """Получает на вход список валют, возвращает список словарей с парами ваалюта:курс"""

    logging_make_list_dict_from_json_data_stocks.info("Старт программы")
    return [{x: get_exchange(x)["exchange_rate"]} for x in list]


def make_list_dict_from_json_data_stocks(list):
    """Получает на вход список названий акций, возвращает список словарей с парами акция:цена"""

    logging_make_list_dict_from_json_data_stocks.info("Старт программы")
    return [{x: get_stock_prices(x)["price"]} for x in list]


def events(start_data, date_range="M"):
    """Программа принимающуая на вход строку с датой и второй необязательный параметр — диапазон данных
    Возвращает JSON-ответ по форме в соответстивии с ТЗ"""
    logging_events.info(f"Запуск программы с параметрами {start_data}, {date_range}")
    # Получаем название файла из дата
    exel_filename = take_filename_from_data()
    logging_events.info(f"Получили название файла с данными {exel_filename}")

    # Получаем предварительные списки по доходам и расходам из файла эксель
    cash_list, expenses_list, expenses_amount = get_data_from_exel(
        exel_filename, 0, start_data, date_range
    )
    income_list, income_amount = get_data_from_exel(
        exel_filename, 1, start_data, date_range
    )
    logging_events.info("Считали данные из эксель-файла")

    # получаем данные из json файла и перерабытываем их получая словари
    currencies_list, stocks_list = take_data_from_json()
    currencies_list_dict = make_list_dict_from_json_data_currencies(currencies_list)
    stocks_list_dict = make_list_dict_from_json_data_stocks(stocks_list)
    logging_events.info("Считали данные из json")

    # Перерабатываем полученные данные в формат соответствующий заданию
    expenses_list = make_list_dict_by_task(expenses_list, "category", "amount")
    cash_list = make_list_dict_by_task(cash_list, "category", "amount")
    income_list = make_list_dict_by_task(income_list, "category", "amount")
    currencies_list_dict_by_task = make_list_dict_by_task(
        currencies_list_dict, "currency", "rate"
    )
    stocks_list_dict_by_task = make_list_dict_by_task(
        stocks_list_dict, "stock", "price"
    )

    # собираем вложенный словарь по расходам
    expenses_dict = {}
    expenses_dict["total_amount"] = expenses_amount
    expenses_dict["main"] = expenses_list
    expenses_dict["transfers_and_cash"] = cash_list

    # собираем вложенный словарь по доходам
    income_dict = {}
    income_dict["total_amount"] = income_amount
    income_dict["main"] = income_list

    # собираем словарь который будет выводиться
    return_dict = {}
    return_dict["expenses"] = expenses_dict
    return_dict["income"] = income_dict
    return_dict["currency_rates"] = currencies_list_dict_by_task
    return_dict["stock_prices"] = stocks_list_dict_by_task
    logging_events.info("Сформирован слвоарь для заливны в json")

    json_data = json.dumps(return_dict, ensure_ascii=False, indent=4)
    logging_events.info("Функция отработала корректно")
    print(json_data)
