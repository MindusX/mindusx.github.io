from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from .models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')


class SMSForm(FlaskForm):
    to_number = StringField('Numéro destinataire', validators=[DataRequired(), Length(min=10, max=20)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=160)])
    submit = SubmitField('Envoyer')