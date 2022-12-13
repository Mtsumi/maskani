from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required
#, logout_user, 
from .forms import RegisterForm, LoginForm
from . import app, db



from .models import *


db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=hashed_password,
                    role=form.role.data)
        db.session.add(user)
        db.session.commit()
        #print(f'I am a ' + {user.role})
        if user.role=='client': 
            new_user = Client(user_id=user.id)
            print('Creating a "client" object and logging the user in')
        else:
            new_user= Fundi(user_id=user.id)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register to Maskani', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            user_id = user.id
            if user.role == 'fundi':
                
                specific_user = Fundi.query.filter_by(user_id=user_id).first()
            else:
                specific_user = Client.query.filter_by(user_id=user_id).first()
            login_user(specific_user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Maskani Login', form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_authenticated:
        if current_user.user.role == 'fundi':
            print(current_user.user.last_name)
            print(current_user.user.role)
            return redirect(url_for('mywork'))
        else:
            print(current_user.user.last_name)
            print(current_user.user.role)
            print(current_user.user.id)
            return redirect(url_for('myorders'))
        
    return("<h1>There is no User here!<h2>")


@app.route("/clients/myorders")
@login_required
def myorders():
    return "<h1>My favourite Gigs on My order Page</h1>"

@app.route("/about")
def about():
    return"<h1>This is the about page</h1>"    

@app.route("/clients/edit")
@login_required
def edit_client():
    return "<h1> This is the where client comes after login <h1>"


@app.route("/fundis/edit")
@login_required
def edit_fundi():
    return "<h1> This is the where Fundi comes after login <h1>"

@app.route("/fundis/mywork")
@login_required
def mywork():
    return "<h1>My Jobs</h1>"

@app.route("/get_started")
def get_started():
    return render_template("get_started.html")
