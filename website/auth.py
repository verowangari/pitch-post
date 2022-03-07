from crypt import methods
from flask import Blueprint,render_template,redirect, request, url_for 

auth=Blueprint("auth",__name__)

@auth.route("/login")
def login():
    email=request.form.get("email")
    password1=request.form.get("password1")
    return render_template("login.html", methods=['GET','POST'])

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    email=request.form.get("email")
    username=request.form.get("username")
    password1=request.form.get("password1")
    password2=request.form.get("password2")
    print(username)
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))