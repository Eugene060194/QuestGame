from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, StringField
from wtforms.validators import InputRequired, NumberRange, Length


class QuestForm(FlaskForm):
    """Форма для сбора игровых данных.
    """
    side_of_world = SelectField('Выберите сторону света, в которую желаете отправиться',
                                coerce=int,
                                choices=[(0, 'Север'), (1, 'Юг'), (2, 'Запад'), (3, 'Восток')]
                                )
    step_value = IntegerField('Как далеко планируется продвинуться?', default=1,
                              validators=[NumberRange(min=1), InputRequired()])
    submit_button = SubmitField('В путь!')


class RegistrationForm(FlaskForm):
    """Форма для регистрации игрока.
    """
    player_name = StringField('Как вас зовут?', validators=[Length(min=4, max=18), InputRequired()])
    submit_button = SubmitField('Принять')
