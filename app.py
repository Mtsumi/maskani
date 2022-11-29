from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanFieldfrom
from wtforms.validators import InputRequired,Email,lentgh
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!' 
app.config.from_object('config')

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.'.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)