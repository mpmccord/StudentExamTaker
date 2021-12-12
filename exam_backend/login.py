from flask import request, Blueprint
# from . import app
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
login_stuff = Blueprint('login_stuff', __name__)
from password_strength import PasswordPolicy, PasswordStats
# login_manager = LoginManager()
# login_manager.init_app(login_stuff)

"""
Validator for passwords: checks if there is punctuation in the string
@param my_str: a string
@return: boolean: whether the string has punctuation.
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

