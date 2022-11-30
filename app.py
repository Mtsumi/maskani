from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
    return render_template("pages/index.html")
=======
    return render_template('index.html')

>>>>>>> 08326fc (update of tempate)

if __name__ == '__main__':
    app.run(debug=True)
