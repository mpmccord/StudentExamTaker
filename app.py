from flask import Flask, render_template, redirect, url_for, request
#from Cryptography.StudentExamTaker.templates.login import RegistrationForm

import flask
from flask import Flask, render_template, request
import flask_login
import os
from exam_backend.login import *
from werkzeug.security import generate_password_hash

from exam_backend import models
from exam_backend.models import User
from exam_backend.models import db
from exam_backend import create_app
from flask_migrate import Migrate

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def createDatabase():
    db.create_all()
    """
    new_user = User(email="foo.bar@my_email.com", password=generate_password_hash("secret", method='sha256'), school = "University of South Florida", type_account = "Teacher")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    """

@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template("login.html")
    email = flask.request.form['email']
    if email not in users:
        return render_template("bad-login.html")
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return render_template("bad-login.html")


"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'
"""


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

from exam_backend import models
from exam_backend.models import User
from exam_backend.models import db
from exam_backend import create_app
from flask_migrate import Migrate

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def createDatabase():
    db.create_all()
    """
    new_user = User(email="foo.bar@my_email.com", password=generate_password_hash("secret", method='sha256'), school = "University of South Florida", type_account = "Teacher")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    """

if __name__ == '__main__':
    app.run(port=5685, debug=True)
