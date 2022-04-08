from ast import Pass
from email import message
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Campo obbligatorio!")])
    password = PasswordField('Password', validators=[DataRequired("Campo obbligatorio!")])
    remember_me = BooleanField('Ricordami')
    submit = SubmitField('Accedi')

class PostForm(FlaskForm):
    title = StringField('Titotlo', validators=[DataRequired("Campo obbligatorio!"), Length(max=150, message="La lunghezza del titolo supera i 150 caratteri")])
    subtitle = StringField('Sottotitolo', validators=[Length(max=350, message="La lunghezza del sottotitolo supera i 350 caratteri")])
    content = TextAreaField('Contenuto', validators=[DataRequired("Campo obbligatorio!")])
    submit = SubmitField('Salva')