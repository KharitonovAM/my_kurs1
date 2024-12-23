import pandas as pd
import datetime
from typing import Optional

def take_3_month_before(second_data):
    """Принимает на вход дату и возвращает дату за три месяца до"""
    if second_data.month > 3:
        start_date = second_data.replace(month=second_data.month-3)
    else:
        start_date = second_data.replace(month= (12 - (3-second_data.month)))
    return start_date

def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Принимает на вход датафрейм с операциями, название категории и дату.
    Если дата не передана, то берется текущая дата.
    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""

    #Приводим значения столбца Дата операции к формату data
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    #определяем есть ли дата завершения период отчета и если нет, задаём согласно ТЗ
    if date is None:
        end_data = datetime.datetime.now()
    else:
        end_data = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
    start_data = take_3_month_before(end_data)
    working_dataframe = transactions[transactions['Дата операции']<= end_data]
    working_dataframe = working_dataframe[working_dataframe['Дата операции'] >= start_data]
    working_dataframe = working_dataframe[working_dataframe['Категория']==category]
    return working_dataframe['Сумма операции'].sum()
