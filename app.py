from flask import Flask,render_template

app = Flask(__name__) 
app.config.from_object('config')


@app.route("/")
def index():
    return render_template("pages/index.html")


# @app.route("/www.maskani.tech/login")
# def login_page():
#     email = 
#     password =
#     return render_template("pages/template/index.html",)