from flask_wtf import FlaskForm 
from wtforms import BooleanField, PasswordField, SelectField, SubmitField,  StringField
from wtforms.validators import Email, EqualTo, DataRequired, InputRequired, Length, ValidationError
from .models import *
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, login_user, login_required, logout_user, current_user


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class RegisterForm(FlaskForm):
    
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=200)])
    choices = [('client', 'Client'), ('fundi', 'Fundi')]
    role = SelectField('Role', validators=[DataRequired()], choices=choices)
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
