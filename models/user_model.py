from db import db
from flask_login import UserMixin

class userModel(db.Model,UserMixin):
    __tablename__ = 'userdata'

    id = db.Column(db.Integer,primary_key=True)
    identity_card  = db.Column(db.String(7),nullable=True)
    username=db.Column(db.String(50),nullable=True)
    # last_name=db.Column(db.String(50),nullable=True)
    # email=db.Column(db.String(100),unique=True,nullable=False)
    password_hashed = db.Column(db.String(128),nullable=False)
    salary=db.Column(db.Integer)
    job_role=db.Column(db.String(80),nullable=False)
    pan_card=db.Column(db.String(10),unique=True)
    joining_date=db.Column(db.Date(),nullable=False)