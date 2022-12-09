from . import db
from datetime import datetime, timedelta
#import dateutil.parser

#Creating a class model of Database
class Fundi(db.Model):
	__tablename__ = 'fundis'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	image_link = db.Column(db.String(120), nullable=False, default='default_fundi.jpg')
	password = db.Column(db.String(200), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	service = db.Column(db.String(50), nullable=False)

	jobs = db.relationship("Order", backref = "fundis", lazy=True, cascade="all, delete-orphan")
	
	def __repr__(self):
		return f'<Fundi {self.id} {self.first_name} + {self.last_name}>'


class Client(db.Model):
	"""
	Client model definition"""
	__tablename__ = 'clients'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.String(50), nullable=True)
	email = db.Column(db.String(120), nullable=False)
	image_link = db.Column(db.String(120), nullable=False, default='default.jpg')
	password = db.Column(db.String(200), nullable=False)
	location = db.Column(db.String(50), nullable=True)
	
	orders = db.relationship("Order", backref = "clients", lazy=True, cascade="all, delete-orphan")

	def __repr__(self):
		return f'<Client {self.id} {self.first_name} + {self.last_name}>'


class Order(db.Model):
	"""Order class definition"""
	__tablename__ = 'orders'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(500), nullable=False)
	price_range = db.Column(db.String(50), nullable=False)
	image_link = db.Column(db.String(50), nullable=True)
	status = db.Column(db.Boolean, nullable=False, default=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	date_due = db.Column(db.DateTime, default=date_created + timedelta(hours=6), nullable=False)

	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	fundi_id = db.Column(db.Integer, db.ForeignKey("fundis.id"), nullable=False)
