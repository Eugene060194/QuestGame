from random import randint  # Используется для генерации случаного положения нового игрока


class Game:
    """Содержит логику игры, а так же предоставляет методы для работы
    с ней извне.
    """
    # Словарь для сопоставления координат игрового поля с названиями локаций
    __list_of_locations = {
        (0, 0): '"Спальня"',
        (0, 1): '"Холл"',
        (0, 2): '"Кухня"',
        (1, 0): '"Подземелье"',
        (1, 1): '"Коридор"',
        (1, 2): '"Оружейная"',
        'win': '"Балкон"'
    }
    # Переменные для хранения текста, используемого в процессе игры
    __game_text_1 = """Здравствуйте {}! Вчерашний поход к барону явно удался. Сейчас Вы в пыльной непонятной комнате и 
    ваше состояние после бурной ночи оставляет желать лучшего. Глоток свежего воздуха - вот лучшее решение. 
    Пора пробираться к балкону"""
    __game_text_2 = 'Вы находитесь в комнате {}'
    __game_text_3 = 'Вы не можете идти сюда'
    __game_text_4 = """Вы выбрались на чистый воздух и можете вдохнуть полной грудью. Что же, быть может двинуться 
    к дальнейшим приключениям?"""

    def __init__(self, player_name):
        self.game_status = True  # Определяет состоянии игры. При "False" игра считается завершенной.
        self.player_name = player_name
        self.step_counter = 0  # Счетчик ходов - мера скорости прохождения игры.
        self.__player_position = [randint(0, 1), randint(0, 2)]
        # Словарь игровых описаний. Содержит текстовую информацию о ходе игры.
        self.__game_information = {
            'game_desc': self.__game_text_1.format(self.player_name),
            'cur_loc': '',
            'warning': '',
            'win_desc': ''
        }
        self.__set_start_loc()

    def __set_start_loc(self):
        """
        Метод для занесения в словарь игровых описаний стартового положения игрока.

        :return: -
        """
        key = (self.__player_position[0], self.__player_position[1])
        self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations[key])

    def __move_north(self, step):
        """
        Метод движения игрока на север.
        Так же описывает завершение игры(выход на балкон возможен только при шаге на север)

        :param step: Кол-во шагов
        :return: -
        """
        # Условие завершения игры(выход на балкон)
        if (self.__player_position == [0, 1] and step == 1) or (self.__player_position == [1, 1] and step == 2):
            self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations['win'])
            self.__game_information['warning'] = ''
            self.__game_information['win_desc'] = self.__game_text_4
            self.game_status = False
        # Условие обычного шага на север(без завершения игры)
        else:
            coordinate_y = self.__player_position[0] - step
            if 0 <= coordinate_y <= 1:
                self.__player_position[0] = coordinate_y
                key = (self.__player_position[0], self.__player_position[1])
                self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations[key])
                self.__game_information['warning'] = ''
            else:
                self.__game_information['warning'] = self.__game_text_3

    def __move_south(self, step):
        """
        Метод движения игрока на юг.

        :param step: Кол-во шагов
        :return: -
        """
        coordinate_y = self.__player_position[0] + step
        if 0 <= coordinate_y <= 1:
            self.__player_position[0] = coordinate_y
            key = (self.__player_position[0], self.__player_position[1])
            self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations[key])
            self.__game_information['warning'] = ''
        else:
            self.__game_information['warning'] = self.__game_text_3

    def __move_west(self, step):
        """
        Метод движения игрока на запад.

        :param step: Кол-во шагов
        :return: -
        """
        coordinate_x = self.__player_position[1] - step
        if 0 <= coordinate_x <= 2:
            self.__player_position[1] = coordinate_x
            key = (self.__player_position[0], self.__player_position[1])
            self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations[key])
            self.__game_information['warning'] = ''
        else:
            self.__game_information['warning'] = self.__game_text_3

    def __move_east(self, step):
        """
        Метод движения игрока на восток.

        :param step: Кол-во шагов
        :return: -
        """
        coordinate_x = self.__player_position[1] + step
        if 0 <= coordinate_x <= 2:
            self.__player_position[1] = coordinate_x
            key = (self.__player_position[0], self.__player_position[1])
            self.__game_information['cur_loc'] = self.__game_text_2.format(self.__list_of_locations[key])
            self.__game_information['warning'] = ''
        else:
            self.__game_information['warning'] = self.__game_text_3

    def player_move(self, direction, step):
        """
        Метод движения игрока. Собирает в себе методы move_north, move_south, move_west, move_east.
        Запускает нужный метод в зависимости от выбранного направления.

        :param direction: Направление движения
        :param step: Кол-во шагов
        :return: -
        """
        # Проверка состояния игры. При "game_status == False", метод не будет работать.
        if self.game_status:
            self.step_counter += 1
            self.__game_information['game_desc'] = ''
            list_of_moves = [self.__move_north, self.__move_south, self.__move_west, self.__move_east]
            return list_of_moves[direction](step)
        else:
            pass

    def get_game_information(self):
        """
        Метод для получения текстовой информации о ходе игры.

        :return: Словарь текстовых описаний
        """
        return self.__game_information
