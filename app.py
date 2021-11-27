from flask import Flask, render_template
import flask_login
import os
from login import *

app = Flask(__name__)
app.secret_key = os.urandom(81)
login_manager = flask_login.LoginManager(app)
users = {"mel_m29": "PASSWORD2019", "cpm_29": "PASSWORD2019"}


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


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


if __name__ == "__main__":
    app.run(port=5678)
