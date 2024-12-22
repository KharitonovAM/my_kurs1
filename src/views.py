import pandas as pd
from src.utill_web import make_interval_dates
import datetime
import collections

def get_data_from_exel(filename, type_of_operation, start_data, diap_data):
    '''Функция получает на вход имя файла и тип операции 0 - если нужна информация о расходах, 1 - если нужна информация о доходах'''

    #Формируем предварительно рабочий датафрейм (без учета временного интервала)
    exel_dataframe = pd.read_excel(filename)
    only_real_operations = exel_dataframe[exel_dataframe['Статус'] == 'OK']
    only_real_operations['Дата операции'] = pd.to_datetime(only_real_operations['Дата операции'], format= '%d.%m.%Y %H:%M:%S')

    #получаем интервал дат, в рамках которых будет формировать рабочий датафрейм:
    start_data_interval = make_interval_dates(start_data, diap_data)

    #формируем промежуточный рабочий датафрейм с учетом временных интервалов
    if start_data_interval != 'all_data':
        only_real_operations = only_real_operations[only_real_operations['Дата операции'] >= start_data_interval]
        only_real_operations = only_real_operations[only_real_operations['Дата операции'] <= start_data]

    #формируем датафрейм с учтом того, нужны нам данные по расходам или по доходам
    if type_of_operation == 0:
        dataframe_for_work = only_real_operations[only_real_operations['Сумма платежа'] < 0]
    else:
        dataframe_for_work = only_real_operations[only_real_operations['Сумма платежа'] > 0]

    #получаем общую сумму по операциям в рабочем датафрейме
    total_summ = dataframe_for_work['Сумма платежа'].sum()

    #получаем список с перечнем категорий
    list_of_categories = list(set(dataframe_for_work['Категория']))

    #формируем список со словарями категория: сумма по категории
    return_list = []
    for item in list_of_categories:
        z = {}
        z[item] = abs(float(dataframe_for_work[dataframe_for_work['Категория'] == item]['Сумма платежа'].sum()))
        return_list.append(z)

    #сортируем список по убыванию суммы по категориям
    return_list = sorted(return_list, key=lambda x: list(x.values())[0], reverse=True)

    #формируем список с данными по расходу наличных выводя их в отдельный список
    if type_of_operation == 0:
        cash_list = [{"Наличные": 0}, {"Переводы": 0}]
        for item in return_list:
            if list(item.keys())[0] =='Наличные':
                cash_list[0]['Наличные'] = list(item.values())[0]
                return_list.remove(item)
            elif list(item.keys())[0] == 'Переводы':
                cash_list[1]['Переводы'] = list(item.values())[0]
                return_list.remove(item)

        #сртируем список наличных по убыванию
        cash_list = sorted(cash_list, key=lambda x: list(x.values())[0], reverse=True)
        # print(cash_list)
        # print(return_list)
        return cash_list, return_list

    # print(return_list)
    return return_list
