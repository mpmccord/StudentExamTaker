import flask
from flask import Flask, render_template
import flask_login
import os
from login import *

app = Flask(__name__)
app.secret_key = os.urandom(81)
login_manager = flask_login.LoginManager(app)

# Temporary: for testing purposes only
users = {'foo@bar.tld': {'password': 'secret'}}


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template("login.html")
    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


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


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


if __name__ == "__main__":
    app.run(port=5678)
