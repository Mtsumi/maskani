import os


class Config(object):
    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = True

    # Connect to the database
    DATABASE_NAME = 'maskani'
<<<<<<< HEAD
    username = 'oyaro'
    password = 'serverless'
=======
    username = 'postgres'
    password = 'ikxi0000'
>>>>>>> main
    url = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        username,
        password,
        url,
        DATABASE_NAME
    )

    # CSRF token with wtforms
    #WTF_CSRF_ENABLED = True
<<<<<<< HEAD
    #WTF_CSRF_SECRET_KEY = 'wtf secret key'
=======
    #WTF_CSRF_SECRET_KEY = 'wtf secret key'
>>>>>>> main
