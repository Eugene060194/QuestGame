from os import environ  # Используется для получения секретного ключа


class Config(object):
    """Содержит секретный ключ, а так же переменные для подключения
    к SQL-серверу (пароль лежит в "password.py").
    """
    SECRET_KEY = environ.get('SECRET_KEY') or 'any_key'
    host = 'localhost'
    port = 3306
    user = 'root'
    db_name = 'questgame'
