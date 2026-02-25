import pandas as pd

def input_from_console():
    """
    Зчитує текст, введений користувачем з консолі.
    """
    return input("Введіть ваш текст: ")

def read_from_file_builtin(file_path):
    """
    Зчитує вміст файлу за допомогою вбудованих можливостей Python.
    :param file_path: Шлях до текстового файлу.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_from_file_pandas(file_path):
    """
    Зчитує вміст файлу за допомогою бібліотеки pandas.
    :param file_path: Шлях до файлу (наприклад, CSV).
    """
    df = pd.read_csv(file_path)
    return df.to_string()