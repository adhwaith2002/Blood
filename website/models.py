from . import db 
from flask_login import UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class Blood(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.String(200), nullable=False)
    bloodgroup = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    Lastdonationdate = db.Column(db.DateTime)
    userrole =db.Column(db.Integer)
    






