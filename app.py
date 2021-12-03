<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for, request
#from Cryptography.StudentExamTaker.templates.login import RegistrationForm
=======
import flask
from flask import Flask, render_template
import flask_login
import os
from login import *
>>>>>>> 9dafebc32419fa97c0eb85fa1cfd7f1be81efa3e

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
<<<<<<< HEAD
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/teacher_home'))
    return render_template('login.html', error=error)
=======
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
>>>>>>> 9dafebc32419fa97c0eb85fa1cfd7f1be81efa3e


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


<<<<<<< HEAD
=======
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

>>>>>>> 9dafebc32419fa97c0eb85fa1cfd7f1be81efa3e

if __name__ == "__main__":
    app.run(port=5678)
