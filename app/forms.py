from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    text=StringField("Email: ", validators=[Email()])
    '''
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    '''
    submit = SubmitField("Submit")