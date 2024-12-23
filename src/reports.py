import pandas as pd
import datetime
from typing import Optional
from src.decoretors import report_log
from logs.logs_settint import mylogconfig
import logging

# импортируем настройки логирования
logging.basicConfig = mylogconfig

# определяем именные логеры
logging_take_3_month_before = logging.getLogger("logging_take_3_month_before")
logging_spending_by_category = logging.getLogger("logging_tspending_by_category")


def take_3_month_before(second_data):
    logging_take_3_month_before.info("Запуск функции")
    """Принимает на вход дату и возвращает дату за три месяца до"""
    # Определяем, если на входе месяц с апреля по декабрь
    if second_data.month > 3:
        logging_take_3_month_before.info("Определили что индекс месяца более 3")
        start_date = second_data.replace(month=second_data.month - 3)
    # определяем что на входе месяц с января по март
    else:
        logging_take_3_month_before.info("Определили что индекс месяца менее 4")
        start_date = second_data.replace(
            year=(second_data.year - 1), month=(12 - (3 - second_data.month))
        )
    logging_take_3_month_before.info("Функция усппешно завершила свою работу")
    return start_date


@report_log
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    """Принимает на вход датафрейм с операциями, название категории и дату.
    Если дата не передана, то берется текущая дата.
    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)
    """

    logging_spending_by_category.info("Запуск функции")
    # Приводим значения столбца Дата операции к формату data
    transactions["Дата операции"] = pd.to_datetime(
        transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )
    # определяем есть ли дата завершения период отчета и если нет, задаём согласно ТЗ
    if date is None:
        logging_spending_by_category.info("Определили, что дата не передана")
        end_data = datetime.datetime.now()
    else:
        logging_spending_by_category.info("Определили, что дата передана")
        end_data = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
    # Получаем данные по началу интервала
    logging_spending_by_category.info("Присиупаем к получениию начала интервала")
    start_data = take_3_month_before(end_data)
    # Формируем рабочий датафрейм
    logging_spending_by_category.info("Приступаем к формированию датафрема")
    working_dataframe = transactions[transactions["Дата операции"] <= end_data]
    working_dataframe = working_dataframe[
        working_dataframe["Дата операции"] >= start_data
    ]
    working_dataframe = working_dataframe[working_dataframe["Категория"] == category]
    logging_spending_by_category.info("Датафрейм сформирован, программа завершается")
    return working_dataframe["Сумма операции"].sum()


print(take_3_month_before(datetime.datetime(2024, 1, 1, 0, 0, 0)))
