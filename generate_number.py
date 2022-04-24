from string import ascii_letters, digits  # Списки символов
from random import sample  # Метод генерации случайной строки


def generate_number():
    """
    Функция создания номера игровой сессии

    :return: Случайная число-буквенная строка из 8 символов
    """
    symbols = ascii_letters + digits
    return ''.join(sample(symbols, 8))
