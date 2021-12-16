from wtforms.fields.simple import SubmitField
from .models import User, Course, Exam
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
class CreateNewClassForm(FlaskForm):
    name = StringField("Course Title")
    submit = SubmitField("Add Course")

class CreateNewExamForm(FlaskForm):
    name = StringField("Exam Name")
    questions = StringField("Enter your questions: ")
    submit = SubmitField("Create Exam")

