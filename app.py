from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required
#, logout_user, 
from .forms import RegisterForm, LoginForm, OrderForm
from . import app, db



from .models import *


app.app_context().push()
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
        if user.role=='client': 
            new_user = Client(user_id=user.id)
            print('Creating a "fundi" object and logging the user in')
        else:
            new_user = Fundi(user_id=user.id)
            print('Creating a "fundi" object and logging the user in')
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Your account has been created! You can now post a job. You are now able to log in', 'success')
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
        
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            user_id = user.id
            if user.role == 'fundi':
                specific_obj = Fundi.query.filter_by(user_id=user_id).first()
            else:
                specific_obj = Client.query.filter_by(user_id=user_id).first()

            login_user(specific_obj, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Maskani Login', form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_authenticated:
        user= User.query.get(current_user.user_id)
        if user.role == 'fundi':
            print(user.last_name)
            print(user.role)
            return redirect(url_for('mywork'))
        else:
            print(user.last_name)
            print(user.role)
            return redirect(url_for('myorders'))
        
    return("<h1>There is no User here!<h2>")

@app.route("/clients/<int:client_id>/post_a_job", methods=['GET', 'POST'])
@login_required
def new_order(client_id):
    client_id = current_user.get_id()
    user_id = current_user.user_id
    
    print(user_id)
    user = User.query.get(user_id)
    name = user.first_name

    form = OrderForm()
    print(client_id)
    if form.validate():
        print("form validates")
        try:
            new_order = Order(title=form.title.data,
                    description=form.description.data,
                    location=form.location.data,
                    service=form.service.data,
                    image_link=form.image_link.data,
                    price_range=form.price_range.data,
                    #date_due=form.date_due.data,
                    client_id = client_id
                    )
            print(new_order)
            db.session.add(new_order)
            db.session.commit()
            flash("New order " + request.form["title"] + " was successfully listed!")
        except Exception:
            db.session.rollback()
            flash("Order was not successfully listed.")
        finally:
            db.session.close()

    return render_template("new_order.html", title='Post a job', form=form, name=name ) 


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
