from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, InputRequired, Length, Optional, Regexp, URL
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    
    first_name = StringField(
        'First Name', 
        validators=[
            InputRequired(), 
            Length(min=4, max=15)])
    last_name = StringField(
        'Last Name', 
        validators=[
            InputRequired(),
            Length(min=4, max=15)])
    email = StringField(
        'Email',
        validators=[
            InputRequired(), 
            Email(message='Invalid email'), 
            Length(max=50)])
    password = PasswordField(
        'Password', 
        validators=[
            InputRequired(), 
            Length(min=8, max=80)])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(), 
            EqualTo('password')])
    image_link = image_link = StringField(
        'Image link',
        default='',
        validators=[
            Optional(),
            URL()]
    )
    phone_number = StringField(
        'Phone Number',
        validators=[
            InputRequired(),
            Regexp('^[0-9]{3}[-][0-9]{3}[-][0-9]{4}$',
            message='phone number must be in format xxx-xxx-xxxx'
            )
        ]
    )
    location = SelectField(
        'Location', 
        validators=[
            DataRequired()],
        choices=[
            ('Nyali', 'nyali'),
            ('Kisauni', 'Bamburi'), 
            ('Mtwapa','Shanzu'), 
            ('Changamwe', 'Magongo'), 
            ('Likoni', 'Caltex')])
    submit = SubmitField('Sign Up')