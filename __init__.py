from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# App Config.

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

<<<<<<< HEAD
db = SQLAlchemy(app)
app.app_context().push()
=======
db = SQLAlchemy(app)
login_manager = LoginManager(app)
