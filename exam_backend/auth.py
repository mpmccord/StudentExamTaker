# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .models import db
from .login import LoginForm, RegistrationForm
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    school = request.form.get('school')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password) or not school == user.school:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        school = request.form.get('school')
        type_account = request.form.get("type-account")
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email=email, school = school, type_account = type_account, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        return render_template("signup.html", form=form)
"""
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data,
                    password=generate_password_hash(form.password.data, "sha256"), 
                    school=form.school.data, type_account = form.type_account.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)"""
"""if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        school = request.form.get('school')
        type_account = request.form.get("type-account")
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email=email, school = school, type_account = type_account, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        return render_template("signup.html")
"""

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@login_required
@auth.route("/teacher")
def load_teacher():
    if current_user.type_account == "Teacher":
        return render_template("teacher_home.html")