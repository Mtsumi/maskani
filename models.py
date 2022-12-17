from . import db, login_manager
from datetime import datetime, timedelta
from flask_login import UserMixin
#import dateutil.parser

@login_manager.user_loader
def load_user(user_id):

    user = User.query.get(user_id)
    if user is not None:
        if user.role == 'client':
            return Client(user_id=user_id)
        elif user.role == 'fundi':
            return Fundi(user_id=user_id)
    # Return None if the user object is None
    return None


#Creating a class model of Database

class User(db.Model, UserMixin):
    
	id = db.Column(db.Integer, primary_key=True, unique=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(200), nullable=False)
	role = db.Column(db.String(40), nullable=False)
	image_link = db.Column(db.String(120), nullable=False, default='/static/img/default.jpg')
	phone_number = db.Column(db.String(50), nullable=True)
	location = db.Column(db.String(50), nullable=True)

	fundis = db.relationship('Fundi', backref = "user", lazy=True)
	clients = db.relationship('Client', backref = "user", lazy=True)




class Fundi(db.Model, UserMixin):
	__tablename__ = 'fundis'

	id = db.Column(db.Integer, primary_key=True)
	skills = db.Column(db.String(50), nullable=True)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	jobs = db.relationship("Order", backref = "fundis", lazy=True)
	
# This property returns the User object associated with this Fundi object
	@property
	def user(self):
		return User.query.get(self.user_id)

	def __repr__(self):
# Use the user property to access the first_name and last_name attributes
		return f'<Fundi {self.id} {self.user.first_name} + {self.user.last_name}>'

class Client(db.Model, UserMixin):
	"""
	Client model definition"""
	__tablename__ = 'clients'

	id = db.Column(db.Integer, primary_key=True)
	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	orders = db.relationship("Order", backref = "clients", lazy=True)
	
	@property
	def user(self):
		return User.query.get(self.user_id)

	def __repr__(self):
# Use the user property to access the first_name and last_name attributes
		return f'<Fundi {self.id} {self.user.first_name} + {self.user.last_name}>'

class Order(db.Model):
	"""Order class definition"""
	__tablename__ = 'orders'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(500), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	price_range = db.Column(db.String(50), nullable=False)
	image_link = db.Column(db.String(50), nullable=True)
	status = db.Column(db.Boolean, nullable=False, default=False)
	service = db.Column(db.String, nullable=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	date_due = db.Column(db.DateTime, default=date_created + timedelta(hours=6), nullable=False)

	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	fundi_id = db.Column(db.Integer, db.ForeignKey("fundis.id"), nullable=False)
	
	
	@property
	def user(self):
		
		return User.query.get(self.iden)

	def __repr__(self):
		return f'<Order {self.id} {self.user.first_name} + {self.user.last_name}>'
