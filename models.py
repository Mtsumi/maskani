from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQlAlchemy(app)

#Creating a class model of Database
class Fundi(db.Model):
    """ Fundi Model"""
	__tablename__ = 'fundis'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.Integer(50), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	image_link = db.Column(db.String(500))
	password = db.Column(db.String(120), nullable=False)
	location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=False)

	jobs = db.relationship("Order", backref = "fundis", lazy=True, cascade="all, delete-orphan")
	service = db.relationship("Service", backref="fundi", lazy=True, cascade="all, delete-orphan")

class Client(db.Model):
	"""
	Client model definition"""
	__tablename__ = 'clients'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	phone_number = db.Column(db.Integer(50), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	image_link = db.Column(db.String(500))
	password = db.Column(db.String(120), nullable=False)
	location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

	orders = db.relationship("Order", backref = "orders", lazy=True, cascade="all, delete-orphan")

class Order(db.Model):
	"""
	Order class definition
	"""
	__tablename__ = 'orders'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(500), nullable=False)
	price = db.Column(db.String(50), nullable=False)
	image_link = db.Column(db.String(500))
	status = db.Column(db.Boolean, nullable=False, Default=False )
	date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	date_due = db.Column(db.DateTime, default=datetime.utcnow + 5*, nullable=False)

	location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	fundi_id = db.Column(db.Integer, db.ForeignKey("fundis.id"), nullable=False)
	service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)


class Service(db.Model):
	"""Class defines Services that can be offered by fundis"""

	__tablename__ = 'services'

	id = db.Column(db.Integer, primary_key=True)
	service_name = db.Column(db.String(50), primary_key=True)
	fundi_id = db.Column(db.Integer, db.ForeignKey("fundis.id"), nullable=False)
	orders = db.Relationship("Order", backref="orders", lazy=True, nullable=False)

class Location(db.Model):
	""" Defines location model"""
	__tablename__ = 'locations'

	id = db.Column(db.Integer, primary_key=True)
	county = db.Column(db.String(50), nullable=False)
	sub_county = db.Column(db.String(50), nullable=False)

	clients = db.Relationship("Client", backref="clients", lazy=True, nullable=False)
	fundis = db.Relationship("Fundi", backref="fundis", lazy=True, nullable=False)
	orders = db.Relationship("Order", backref="orders", lazy=True, nullable=False)
