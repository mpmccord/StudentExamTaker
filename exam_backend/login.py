from flask import request, Blueprint
# from . import app
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp
login_stuff = Blueprint('login_stuff', __name__)
import string
import re
# login_manager = LoginManager()
# login_manager.init_app(login_stuff)

"""
class RegistrationForm(FlaskForm):
    username = TextAreaField('Username', [validators.Length(min=4, max=20)])
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        DataRequired(),
        # validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', DataRequired())#, [validators.Required()])
"""
"""
Validator for passwords: checks if there is punctuation in the string
@param my_str: a string
@return: boolean: whether the string has punctuation.
"""
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), Email("Please enter a valid email")])
    password = PasswordField('New Password', [
        validators.length(min=8, message = "Password must be at least 8 characters"),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        Regexp(regex="[0-9]", message="Must have at least one digit"),
        Regexp(regex="\w+", message="Must have at least one special character")
    ])
    confirm = PasswordField('Repeat Password')
    schools = ["New College of Florida", "University of South Florida", "Florida International University"]
    school = SelectField("School", [DataRequired()], choices=schools)
    type_account = ["Teacher"]
    # type_accounts = SelectField("Account", [DataRequired()], choices=type_accounts)
    type_accounts = RadioField("Account", validators=[DataRequired()], choices = type_account)
    accept_tos = BooleanField('I accept the TOS', [DataRequired()])

class LoginForm(FlaskForm):
    username = TextAreaField('Username', [validators.Length(min=4, max=20)])
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        DataRequired(),
        validators.length(min=8),

        validators.EqualTo('confirm', message='Passwords must match')
    ])
    choices = ["New College of Florida", "University of South Florida", "Florida International University"]
    school = SelectField("School", DataRequired(), choices=choices)
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', DataRequired())#, [validators.Required()])

@login_stuff.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data



    except Exception as e:
        return(str(e))

