from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required
#, logout_user, 
from .forms import RegisterForm, LoginForm
from . import app, db



from .models import *


app.app_context().push()
db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_authenticated:
        user = current_user
        if user.user.role == 'fundi':
            return redirect(url_for('mywork'))
        else:
            return redirect(url_for('myorders'))
    return("<h1>There is no User here!<h2>")

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
        print(f'I am a {user["role"]}')
        if user.role=='client': 
            new_client = Client(user_id=user.id)
            print('Creating a "client" object and logging the user in')
            db.session.add(new_client)
            db.session.commit()
            login_user(new_client, remember=True)
            flash('Your account has been created! You can now post a job. You are now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            new_fundi = Fundi(user_id=user.id)
            print('Creating a "fundi" object and logging the user in')
            db.session.add(new_fundi)
            db.session.commit()
            login_user(new_fundi, remember=True)
            flash('Your account has been created! You are now a Fundi at Maskani. You are now able to log in', 'success')
            return redirect(url_for('login'))

    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register to Maskani', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    print(current_user._get_current_object)
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
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

@app.route("/clients/login")
def client_login():
    return "<h1>This is the login route</h1>"

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
