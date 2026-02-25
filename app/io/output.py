import pandas as pd

def output_to_console(data):
    """
    Виводить отримані дані у консоль.
    :param data: Текст або об'єкт для виводу.
    """
    print(data)

def write_to_file_builtin(data, file_path):
    """
    Записує текст у файл за допомогою вбудованих можливостей Python.
    :param data: Текст для запису.
    :param file_path: Шлях до файлу.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(data))

def write_to_file_pandas(df, file_path):
    """
    Записує DataFrame у CSV файл за допомогою pandas.
    :param df: Pandas DataFrame або дані, які можна конвертувати.
    :param file_path: Шлях до файлу.
    """
    if not isinstance(df, pd.DataFrame):
        # Якщо передано просто текст, перетворимо його в таблицю для запису
        df = pd.DataFrame([df])
    df.to_csv(file_path, index=False)