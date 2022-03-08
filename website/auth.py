from crypt import methods
from distutils.log import error
from flask import Blueprint,render_template,redirect, request, url_for,flash 
from . import db
from .models import User

auth=Blueprint("auth",__name__)

@auth.route("/login")
def login():
    email=request.form.get("email")
    password1=request.form.get("password1")
    return render_template("login.html", methods=['GET','POST'])

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
   
        email=request.form.get("email")
        username=request.form.get("username")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        
        email_exists=User.query.filter_by(email=email).first()
        username_exists=User.query.filter_by(username=username).first()
        if email_exists:
            flash('The email already exists!', category='error')
        elif username_exists:
            flash("The Username already exists",category='error')
        
        elif password1!=password2:
            flash('Password mismatch',category='error')
        
        elif len(username) <3:
            flash('Username too short!',category='error')
        
        elif len(password1) <8:
            flash('Password too short!',category=error)
            
        elif len(email)<5:
            flash('Email is invalid',category='error')
            
        else:
            new_user=User(email=email,username=username,password=password1)
            
            
        
    
    # print(username)
    # print(email)
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))