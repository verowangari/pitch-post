from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required, current_user
from .models import Pitch,User,Comment
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

@views.route("/delete-pitch/<id>")
@login_required
def delete_pitch(id):
    pitch = Pitch.query.filter_by(id=id).first()

    if not pitch:
        flash("Post does not exist.", category='error')
    elif current_user.id != pitch.id:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(pitch)
        db.session.commit()
        flash('Pitch deleted.', category='success')

    return redirect(url_for('views.home'))

@views.route("/pitches/<username>")
@login_required
def pitches(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    pitches=user.pitches
    return render_template("pitch.html", user=current_user, pitches=pitches, username=username)

@views.route("/create-comment/<pitch_id>", methods=['POST'])
@login_required
def create_comment(pitch_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        pitch = Pitch.query.filter_by(id=pitch_id)
        if pitch:
            comment = Comment(
                text=text, author=current_user.id, pitch_id=pitch_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist.', category='error')

    return redirect(url_for('views.home'))
