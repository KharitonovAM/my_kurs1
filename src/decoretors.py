from src.setting import Reports_log
from logs.logs_settint import mylogconfig
import logging

# импортируем настройки логирования
logging.basicConfig = mylogconfig

# определяем именные логеры
logging_report_log = logging.getLogger("decorator_report_log")


def report_log(func):
    def wrapper(*args, **kwargs):
        logging_report_log.info("Начало выполнение декоратора")
        rezult = func(*args, **kwargs)
        with open(Reports_log, "a", encoding="utf-8") as f:
            f.write(f"Выполнен отчёт {func.__name__}, результат отчёта {rezult}\n")
        return rezult

    logging_report_log.info("Декоратор отработал нормально")
    return wrapper
