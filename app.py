import os
import secrets
from PIL import Image
from flask import render_template, request, flash, redirect, url_for,abort
from .models import Order
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user 

#, logout_user, 

from .forms import RegisterForm, LoginForm, OrderForm, UpdateAccountForm
from . import app, db

from .models import *


app.app_context().push()
db.create_all()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/clients/sign_up", methods=['GET', 'POST'])
def client_sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        try :
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        role='client')
            db.session.add(user)
            db.session.commit()
            print('Creating a "client" object and logging the user in')
            client = Client(user_id=user.id)
            db.session.add(client)
            db.session.commit()
            flash('Your account has been created! You can now post a job. You are now able to log in', 'success')
        except:
            db.session.rollback()
            flash("Sign Up failed!")
        finally:
            db.session.close()
            return redirect(url_for('login'))
    return render_template('sign_up.html', title='Register As a Client', form=form)
    

@app.route("/fundis/sign_up", methods=['GET', 'POST'])
def fundi_sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        try :
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        role='fundi')
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can claim jobs. You are now able to log in', 'success')
        except:
            db.session.rollback()
            flash("Sign Up failed!")
        finally:
            db.session.close()
            return redirect(url_for('login'))
    return render_template('sign_up.html', title='Register As a Fundi', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    print(current_user._get_current_object)
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Maskani Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_authenticated:
        if current_user.role == 'fundi':
            print(current_user.last_name)
            print(current_user.role)
            return redirect(url_for('mywork'))
        else:
            print(current_user.last_name)
            print(current_user.role)
            return redirect(url_for('myorders'))
        
    return("<h1>There is no User here!<h2>")

@app.route("/clients/post_a_job", methods=['GET', 'POST'])
@login_required
def new_order():
    if current_user.is_authenticated:
        #creating a variable user_id an initialize with current_user id
        user_id = current_user.id
        #print the user_id 
        print(user_id)
        #Query the client and check if user_id(foreign key from client table) =user_is
        client = Client.query.filter_by(user_id=user_id).first()
        #print the client varible
        print(client)   
        print(f"client ID is {client.id}")
        name = current_user.first_name
        print(f"Client name is {name}")
        #creating an instance of the form
        form = OrderForm()
        if form.validate_on_submit():
            print("form validates")
            #validate the field data before exception
            try:
                order = Order(title=form.title.data,
                            description=form.description.data,
                            location=form.location.data,
                            service=form.service.data,
                            image_link=form.image_link.data,
                            price_range=form.price_range.data,
                            client_id = client.id
                            )
                print(order)
                #A_dd and commit the order properties into oder object in the database
                db.session.add(order)
                db.session.commit()
                flash("New order " + request.form["title"] + " was successfully listed!")
            except Exception:
                db.session.rollback()
                flash("Order was not successfully listed.")
            finally:
                db.session.close()
                return redirect(url_for('myorders'))
        print("<h1>Form Validation failed<h1>")

        return render_template("new_order.html", title='Post a job', form=form, name=name )


    return ("<h1>User isn't logged in<h1>")

@app.route("/clients/account", methods=['GET', 'POST'])
@login_required
def account():
    if current_user.is_authenticated:
        # Get the currently logged-in user object
        user = current_user
        #creating a variable for rendering user in jinja template.
        name = user.username
        #creating an instance of UpdateAccountForm
        form = UpdateAccountForm()
        if form.validate_on_submit():
            # Update the user's data with the form data
            try:    
                user.username = form.username.data
                user.email = form.email.data
                if form.picture.data:
                    # Save the new profile picture and update the user's image_link field
                    picture_file = save_picture(form.picture.data)
                    user.image_link = picture_file

                # Commit the changes to the database
                db.session.commit()
                flash('Your account has been updated!', 'success')
            except:
                db.session.rollback()
                flash("Account was not successfully updated.")
            finally:
                db.session.close()
            return redirect(url_for('account'))
        elif request.method == 'GET':
            # Prefill the form with the current data of the user
            form.username.data = user.username
            form.email.data = user.email
        image_link = url_for('static', filename='img/' + user.image_link)
        return render_template('account.html', title='Account',
                            image_link=image_link, form=form, name=name)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn                           

@app.route("/clients/myorders")
@login_required
def myorders():
    #creating a variable and initializing it with current_id
    user_id = current_user.id
    #Query the client and compare the User_id = user_id
    client = Client.query.filter_by(user_id=user_id).first_or_404()

    orders = Order.query.filter_by(client_id=client.id)
    return render_template('myorders.html', orders=orders)

    

@app.route("/order/<int:order_id>/update", methods=['GET', 'POST'])
@login_required
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user != current_user:
        abort(403)
    form = OrderForm()
    if form.validate_on_submit():
        order.title = form.title.data
        order.description = form.description.data
        db.session.commit()
        flash('Your Order has been updated!', 'success')
        return redirect(url_for('order', order_id=order.id))
    elif request.method == 'GET':
        form.title.data = order.title
        form.description.data = order.description
    return render_template('new_order.html', title='Update Order',
                           form=form, legend='Update Order')

@app.route("/order/<int:order_id>")
def order(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order.html', title=order.title, order=order)

@app.route("/order/<int:order_id>/delete", methods=['POST'])
@login_required
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user != current_user:
        abort(403)
    db.session.delete(order)
    db.session.commit()
    flash('Your Order has been deleted!', 'success')
    return redirect(url_for('myorders'))


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
    #orders = Order.query.all()
    page = request.args.get('page', 1, type=int)
    orders = Order.query.order_by(Order.date_created.desc()).paginate(page=page, per_page=5)
    return render_template('myorders.html', orders=orders)

@app.route("/get_started")
def get_started():
    return render_template("get_started.html")


@app.route("/user/<string:username>")
def client_orders(username):
    #create a query for specific user---using thr username as argument at the function
    page = request.args.get('page', 1, type=int)
    #create a varible that will initialize the user,that we need to query---with first means get the first username ,if nun return 404
    user = User.query.filter_by(username=username).first_or_404()
    #Filter the order --using valiable orders using the user as backref and assign to variable user
    #Using the backslash--breakes th code to multiple line rather than making it longer.
    orders = Order.query.filter_by(user=user)\
        .order_by(Order.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('client_orders.html', orders=orders, user=user)
