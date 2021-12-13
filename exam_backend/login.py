from flask import request, Blueprint
# from . import app
from .models import db, User
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email

"""
User registration form.
- Takes in the username, email, password, school, account type
- Confirms the password is strong enough by using these criteria.
In future, the functions in testing password will be used rather than regexp to incorporate entropy as well.
"""
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), Email("Please enter a valid email")])
    password = PasswordField('New Password', [
        # Must be at least eight characters, at least one uppercase letter, one lowercase letter, one number and one special character
        validators.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", message="Must be at least eight characters, at least one uppercase letter, one lowercase letter, one number and one special character")


    ])
    confirm = PasswordField('Repeat Password')
    schools = ["New College of Florida", "University of South Florida", "Florida International University"]
    school = SelectField("School", [DataRequired()], choices=schools)
    type_account = ["Teacher"]
    type_accounts = RadioField("Account", validators=[DataRequired()], choices = type_account)
    accept_tos = BooleanField('I accept the TOS', [DataRequired()])
"""
User login form.
- Takes in the email, password and school and logs the user in.
"""
class LoginForm(FlaskForm):
    # username = TextAreaField('Username', [validators.Length(min=4, max=20)])
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50), Email()])
    password = PasswordField('Password', [
        DataRequired()
    ])
    choices = ["New College of Florida", "University of South Florida", "Florida International University"]
    school = SelectField("School", [DataRequired()], choices=choices)