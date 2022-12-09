from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
#, login_required, logout_user, current_user
from .forms import ClientRegisterForm, FundiRegisterForm
from . import app, db



from .models import *


#db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")
<<<<<<< HEAD
=======

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

<<<<<<< HEAD
    #         print("niko hapa sai")
            
    #         user = Client.query.filter_by(email=email).first()
    #         if user:
    #             flash('Email already exists.', category='error')
    #         elif len(str(email)) < 4:
    #             flash('Email must be greater than 3 characters.', category='error')
    #         elif len(str(first_name)) < 2:
    #             flash('First name must be greater than 1 character.', category='error')
    #         elif len(str(last_name)) < 2:
    #             flash('Last name must be greater than 1 character.', category='error')
    #         elif password != password2:
    #             flash('Passwords don\'t match.', category='error')
    #         elif len(str(password)) < 7:
    #             flash('Password must be at least 7 characters.', category='error')
    #         else:
    #             print("niko hapa")
    #             new_user = Client(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(
    #                 password, method='sha256'))
    #             print(new_user)
    #             db.session.add(new_user)
    #             db.session.commit()
    #             login_user(new_user, remember=True)
    #             flash('Account succesfully created!', category='success')
    #             return redirect(url_for('edit_client'))
    # except:
    #     db.session.rollback()
    # finally:
    #     db.session.close()

    # return render_template("sign_up.html", form=form)
>>>>>>> main

@app.route('/clients/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = ClientRegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Client(
=======

@app.route('/fundis/sign_up', methods=['GET', 'POST'])
def fundi_signup():
    form = FundiRegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Fundi(
>>>>>>> main
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_password,
<<<<<<< HEAD
=======
                profession=form.profession.data,
>>>>>>> main
                )
        db.session.add(new_user)
        db.session.commit()
        #login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
<<<<<<< HEAD
        return redirect(url_for('edit_client'))
    flash('Something went wrong with validation')
    return render_template('sign_up.html', title='Register', form=form)
=======
        return redirect(url_for('edit_fundi'))
    flash('Something went wrong with validation')
    return render_template('fundi_sign_up.html', title='Register As A Fundi', form=form)
        
>>>>>>> main

        

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

<<<<<<< HEAD
=======
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

<<<<<<< HEAD
>>>>>>> main
=======
@app.route("/fundis/edit")
def edit_fundi():
    return "<h1> This is the where Fundi comes after login <h1>"

@app.route("/fundis/login")
def fundi_login():
    return "<h1>This is the login route for fundis</h1>"
>>>>>>> main
