#from sqlalchemy db object in __init__.py
from enum import unique
from . import db 
from flask_login import UserMixin

# automatically adds the date in line 12
from sqlalchemy.sql import func

class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(150), unique = True)
    date = db.Column(db.DateTime(timezone = True), default= func.now())
    quantity = db.Column(db.Integer)
    image_link = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    cards = db.relationship('Card')