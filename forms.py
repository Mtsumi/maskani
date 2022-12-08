from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, InputRequired, Length,ValidationError
from .models import Client

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class ClientRegisterForm(FlaskForm):
    
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = StringField('Last Name',  validators=[InputRequired(),Length(min=4, max=15)])
    email = StringField('Email',validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

    def validate_email(self,email):
        user=Client.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken,please choose a differnt one.')