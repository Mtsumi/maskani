from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
#, login_required, logout_user, current_user
from .forms import *
from . import app, db



from .models import *


#db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route('/clients/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = ClientRegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Client(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_password,
                )
        db.session.add(new_user)
        db.session.commit()
        #login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('edit_client'))
    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register', form=form)

        

@app.route("/sign")
def sign():
    return render_template("signup.html")

@app.route("/clients/login")
def client_login():
    return "<h1>This is the login route</h1>"

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"

@app.route("/clients/edit")
def edit_client():
    return "<h1> This is the where client comes after login <h1>"

