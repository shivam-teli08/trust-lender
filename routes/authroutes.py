from flask import Blueprint, render_template, request, redirect, url_for, flash
auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/signup')
def signup():
    return render_template("authtemplates/signup.html")
@auth_bp.route('/signin')
def signin():
    return render_template("authtemplates/signin.html")