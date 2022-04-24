from flask import Flask, render_template, request, url_for, redirect
from forms import QuestForm, RegistrationForm
from config import Config
from game_logic import Game
from database_connect import insert_name_into_db, insert_result_into_db
from generate_number import generate_number

QuestGame = Flask(__name__)
QuestGame.config.from_object(Config)

# Словарь для хранения текущих игровых сессий ("номер сессии": "Объект игры",)
sessions_list = {}


@QuestGame.route('/')  # Функция представления стартовой страницы
def index():
    return render_template('index.html')


@QuestGame.route('/registration', methods=['GET', 'POST'])  # Функция представления для страницы регистрации
def registration():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('registration.html', form=form)
    elif request.method == 'POST':
        player_name = request.form.get('player_name')
        session_number = generate_number()
        insert_name_into_db(player_name, session_number)
        sessions_list[session_number] = Game(player_name)
        return redirect(url_for('game', session_number=session_number))


@QuestGame.route('/game/<string:session_number>', methods=['GET', 'POST'])  # Функция представления для страницы игры
def game(session_number):
    form = QuestForm()
    game_session = sessions_list[session_number]
    if request.method == 'GET':
        inf = game_session.get_game_information()
        return render_template('game.html', form=form, **inf)
    elif request.method == 'POST':
        side_of_world = int(request.form.get('side_of_world'))
        step_value = int(request.form.get('step_value'))
        game_session.player_move(side_of_world, step_value)
        inf = game_session.get_game_information()
        # Проверка игры на "законченность"
        if not game_session.game_status:
            insert_result_into_db(game_session.step_counter, session_number)
        return render_template('game.html', form=form, **inf)


if __name__ == '__main__':
    QuestGame.run()
