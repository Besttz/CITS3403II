from flask_wtf import form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required


class LoginForm(form):
    username = StringField("Username", validators=[data_required()])
    password = PasswordField("Password", validators=[data_required()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
