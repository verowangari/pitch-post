from cgitb import text
from unicodedata import category
from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required, current_user
from .models import Pitch
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/create-pitch", methods=['GET', 'POST'])
@login_required
def create_pitch():
    if request.method =="POST":
        text = request.form.get('text')
        
        if not text:
            flash('This cannot be empty',category='error')
        else:
            Pitch=Pitch(text=text,author=current_user.id)
            db.session.add(Pitch)
            db.session.commit()
            flash('Pitch Created!!',category='success')
    
    return render_template('create_pitch.html', user=current_user)