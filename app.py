from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
#, login_required, logout_user, current_user
from .forms import ClientRegisterForm, FundiRegisterForm,LoginForm
from . import app, db



from .models import *


db.create_all()

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
        return redirect(url_for('client_login'))
    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register', form=form)


@app.route('/fundis/sign_up', methods=['GET', 'POST'])
def fundi_signup():
    form = FundiRegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Fundi(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_password,
                profession=form.profession.data,
                )
        db.session.add(new_user)
        db.session.commit()
        #login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('edit_fundi'))
    flash('Something went wrong with validation')
    return render_template('fundi_sign_up.html', title='Register As A Fundi', form=form)
        

@app.route("/sign")
def sign():
    return render_template("signup.html")

#@app.route("/clients/login")
# def client_login():
#    return "<h1>This is the login route</h1>"

@app.route("/clients/login", methods=['GET', 'POST'])
def client_login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hillaryoyaroh@gmail.com' and form.password.data == 'serverless':
            flash('You have been logged in!', 'success')
            return redirect(url_for('mywork'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/clients/mywork")
def mywork():
    return "<h1>My favourite Gigs</h1>"

@app.route("/about")
def about():
    return"<h1>This is the about page</h1>"    

@app.route("/clients/edit")
def edit_client():
    return "<h1> This is the where client comes after login <h1>"

@app.route("/fundis/edit")
def edit_fundi():
    return "<h1> This is the where Fundi comes after login <h1>"

@app.route("/fundis/login")
def fundi_login():
    return "<h1>This is the login route for fundis</h1>"
