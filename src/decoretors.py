from src.setting import Reports_lod
def report_log(func):
    def wrapper(*args,**kwargs):
        rezult = func(*args, **kwargs)
        with open(Reports_lod, 'a', encoding='utf-8') as f:
            f.write(f'Выполнен отчёт {func.__name__}, результат отчёта {rezult}\n')
        return rezult
    return wrapper
