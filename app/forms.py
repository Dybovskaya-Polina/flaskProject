
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

class ContactForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")])
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(),Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
    psw2 = PasswordField("Повтор пароля: ", validators=[DataRequired(), EqualTo('psw', message="Пароли не совпадают")])
    submit = SubmitField("Регистрация")
