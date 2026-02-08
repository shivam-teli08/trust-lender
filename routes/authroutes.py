from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash,check_password_hash
from extensions import db
from database.authmodel import User

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip().lower()
        phone = request.form.get('phone').strip()
        age_str = request.form.get('age').strip()
        password = request.form.get('password').strip()
        confirm_password = request.form.get('confirm password').strip()
        errors = []
        if not age_str:
            errors.append("Age is required")
        elif int(age_str) < 18:
            errors.append("Age should be more than 18")
        if password != confirm_password:
            errors.append("Password not matching with confirmed password")
        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for('auth.signup'))
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists", "error")
            return redirect(url_for("auth.signup"))
        hashed_password = generate_password_hash(password)
        new_user=User(
            name=name,
            email=email,
            phone=phone,
            age=int(age_str),
            auth_provider='local',
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful", "success")
        return redirect(url_for('auth.signin'))    #here hugga
    return render_template("authtemplates/signup.html")    

@auth_bp.route('/signin',methods = ['POST','GET'])
def signin():
    if request.method == 'post':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash("Email and password are required", "error")
            return redirect(url_for('auth.signin'))
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("User not found", "error")
            return redirect(url_for('auth.signin'))
        if not check_password_hash(user.password, password):
            flash("Invalid password", "error")
            return redirect(url_for('auth.signin'))
        flash("Signin successful", "success")
    return render_template("authtemplates/signin.html")          #all good
 

@auth_bp.route('/success')
def successs():
 
    return render_template("success.html")          #iski mkc nikal de