from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email Address :', validators=[Required(), Email()])
    password = PasswordField('Password :', validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address :', validators=[Required(), Email()])
    username = StringField('Enter Username :', validators=[Required()])
    password = PasswordField('Password :', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password :', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("The Email has already been taken!")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("The username has already been taken")
