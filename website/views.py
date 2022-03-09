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
    pitches=Pitch.query.all()
    return render_template("home.html", user=current_user,pitches=pitches)

@views.route("/create-pitch", methods=['GET', 'POST'])
@login_required
def create_pitch():
    if request.method =="POST":
        text = request.form.get('text')
        
        if not text:
            flash('This cannot be empty',category='error')
        else:
            pitch=Pitch(text=text,author=current_user.id)
            db.session.add(pitch)
            db.session.commit()
            flash('Pitch Created!!',category='success')
        return redirect(url_for('views.home'))
    
    return render_template('create_pitch.html', user=current_user)

@views.route("delete-post/<id>")
@login_required
def delete_pitch(id):
    pitch=Pitch.query.filter_by(id=id)
    
    if not pitch:
        flash("Pitch does not exist",category='error')
    elif current_user.id !=pitch.id:
        flash('you do not have permission to delete this pitch')
    else:
        db.session.delete(pitch)
        db.session.commit()
        flash('Pitch deleted',category='success')
        
    return redirect(url_for('views.home'))