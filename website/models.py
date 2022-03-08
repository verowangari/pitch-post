from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model,UserMixin): #Inherits from db model and userMixin
    id=db.Column(db.Interger,primary_key=True)
    email=db.Column(db.String(150),unique=True) #prevent users with duplicate emails
    username=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    date_created=db.Column(db.Date(timezone=True),default=func.now()) #if nothing is passed,by default the column will be filled by the current time