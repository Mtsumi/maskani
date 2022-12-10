from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
#, login_required, logout_user, 
from .forms import ClientRegisterForm, FundiRegisterForm, LoginForm
from . import app, db



from .models import *


db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route('/clients/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('mywork'))
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
        login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('client_login'))
    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register', form=form)


@app.route('/fundis/sign_up', methods=['GET', 'POST'])
def fundi_signup():
    if current_user.is_authenticated:
        return redirect(url_for('mywork'))
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
        


@app.route("/clients/login", methods=['GET', 'POST'])
def client_login():
    if current_user.is_authenticated:
        return redirect(url_for('mywork'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Client.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('edit_client'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Customer Login', form=form)

@app.route("/fundis/login", methods=['GET', 'POST'])
def fundi_login():
    if current_user.is_authenticated:
        return redirect(url_for('mywork'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Fundi.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('edit_fundi'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('fundi_login.html', title='Fundi Login', form=form)

@app.route("/clients/myorders")
def myorders():
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

@app.route("/fundis/mywork")
def mywork():
    return "<h1>My Jobs</h1>"

@app.route("/get_started")
def get_started():
    return render_template("get_started.html")