from flask import request
from . import app
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators
login_manager = LoginManager()
login_manager.init_app(app)


class RegistrationForm(FlaskForm):
    username = TextAreaField('Username', [validators.Length(min=4, max=20)])
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        # validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)')#, [validators.Required()])

@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data



    except Exception as e:
        return(str(e))

