import pymysql
from config import Config

# Блок для перехвата исключения при невозможности импорта конфиг-файла с паролем.
try:
    from password import password  # Содержит пароль для подключения к SQL-серверу
except ImportError:
    password = None


def insert_name_into_db(player_name, session_number):
    """
    Функция для записи в базу данных информации об игроке.

    :param player_name: Имя игрока для записи в БД
    :param session_number: Уникальный номер игровой сессии для записи в БД
    :return: -
    """
    # Блок установки соединения с SQL-сервером
    try:
        connection = pymysql.connect(
            host=Config.host,
            port=Config.port,
            user=Config.user,
            password=password,
            database=Config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        # Блок выполнения запроса на добавление данных в БД
        try:
            with connection.cursor() as cursor:
                request = 'INSERT INTO questgame (player_name, session_Number) VALUES ("{}", "{}")'
                request = request.format(player_name, session_number)
                cursor.execute(request)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print('Failed connect to database...')
        print(ex)


def insert_result_into_db(result, session_number):
    """
    Функция для записи в базу данных игрового результата.

    :param result: Результат игры для записи в БД
    :param session_number: Уникальный номер игровой сессии в БД
    :return: -
    """
    # Блок установки соединения с SQL-сервером
    try:
        connection = pymysql.connect(
            host=Config.host,
            port=Config.port,
            user=Config.user,
            password=password,
            database=Config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        # Блок выполнения запроса на добавление данных в БД
        try:
            with connection.cursor() as cursor:
                request = 'UPDATE questgame SET result={} where session_number="{}"'
                request = request.format(result, session_number)
                cursor.execute(request)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print('Failed connect to database...')
        print(ex)
