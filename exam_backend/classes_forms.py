from wtforms.fields.simple import SubmitField
from .models import User, Course, Exam
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, validators, StringField, FieldList
from wtforms.fields.choices import SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
class CreateNewClassForm(FlaskForm):
    name = StringField("Course Title")
    submit = SubmitField("Add Course")

class CreateNewExamForm(FlaskForm):
    name = StringField("Exam Name")
    questions = StringField("Enter your questions: ")
    submit = SubmitField("Create Exam")

class AnswerForm(FlaskForm):
    answer = StringField("Enter a possible answer: ")
    submit = SubmitField("Enter the answer")

class AddQuestionForm(FlaskForm):
    text = StringField("Enter the text of your question", [validators.DataRequired()])
    # The three possible answers that the user can choose.
    possible_answers = FieldList(StringField("Enter a possible answer: ", [validators.DataRequired()]), min_entries=2)
    # Future expansion: add the correct answer 
    # correct_answer = SelectField("Which is the correct answer?", choices=choices)
    submit = SubmitField("Add Question")

