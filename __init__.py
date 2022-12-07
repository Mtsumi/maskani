from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bootstrap import Bootstrap

# App Config.

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)