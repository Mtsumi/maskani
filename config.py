import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
<<<<<<< HEAD
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/maskani'
#SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
#configuration--database(postgress) and SQLAlchemy
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/maskani'
SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 2ff20838b99e29950448eb1643d89227bdd25d0c
