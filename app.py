from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from auth import *

app = Flask(__name__)
app.register_blueprint(auth)
app.config.from_object('config')
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/sign")
def sign():
    return render_template("signup.html")

@app.route("/clients/<int:client_id>/edit")
def edit_client():
    return "<h1> This is the where client comes after login <h1>"


if __name__ == '__main__':
    app.run(debug=True)
