from .models import User, Course
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError

class CreateNewClassForm(FlaskForm):
    title = StringField("Course Title")

