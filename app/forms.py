from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
# from app.routes import user


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    # preference = SelectField('Which candidates you like?', choices=[
    # ], validators=[DataRequired()], coerce=int)
    submit = SubmitField('Create an account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Repeated username')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Repeated email')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    preference = SelectField('Change the candidate you vote', choices=[
    ], validators=[DataRequired()], coerce=int)
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Repeated username')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Repeated email')

class ManageAccountForm(FlaskForm):
    username = StringField('Name', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    isA = BooleanField('Is Administrator')
    isC = BooleanField('Is Candidate')

    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            if username.data != user.username:
                user = User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('Repeated username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            if email.data != user.email:
                email = User.query.filter_by(email=email.data).first()
                if email:
                    raise ValidationError('Repeated email')
