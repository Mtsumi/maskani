from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
#, login_required, logout_user, current_user
from .forms import *
from . import app, db



from .models import *


db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route('/clients/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Client(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password,
            )
        print("niko hapa")
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('edit_client'))
        
    return render_template('sign_up.html', title='Register', form=form)
        # if request.method == 'POST':
        #     email = request.form.get('email')
        #     first_name = request.form.get('firstName')
        #     last_name = request.form.get('lastName')
        #     password = request.form.get('password')
        #     password2 = request.form.get('password2')

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


@app.route("/sign")
def sign():
    return render_template("signup.html")

@app.route("/clients/login")
def client_login():
    return "<h1>This is the login route</h1>"

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"

@app.route("/clients/<int:client_id>/edit")
def edit_client(client_id):
    return "<h1> This is the where client comes after login <h1>"

