from flask import Flask,render_template
from auth import *

app = Flask(__name__) 
app.register_blueprint(auth)
app.config.from_object('config')


@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/clients/<int:client_id>/edit")
def edit_client():
    return "<h1> This is the where client comes after login <h1>"

