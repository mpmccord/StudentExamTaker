# models.py

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
For now, only creates a teacher account: future expansion will be allowing the user to be a student
Creates a user with email, password and school
@param id: unique id corresponding to the user
"""

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    school = db.Column(db.Text)
    type_account = db.Column(db.Text)

"""
Course corresponding to one teacher where the user is able to create exams.
@param id: the unique id corresponding to the teacher
@param name: The name of the course, ex. Cryptography, Linear Algebra, Abstract Algebra.
@param teacher: The unique id corresponding to the teacher of the course.
@param school: The school where the course takes place.
@param exams: The exams available in the course.
"""

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String, unique = True)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    school = db.Column(db.String)
    questions = db.relationship("User", backref="teacher", lazy = True)
    # exams = db.relationship("Exam", backref="course", lazy = True)

"""
Exams corresponding the course, with specific questions.
@param id: the unique id corresponding to the exam.
@param course: the unique id corresponding to the key (course)
@param questions: the questions on the exam.
"""
"""
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    teacher = db.Column(db.Integer)
    questions = db.relationship("Question", backref="exam", lazy = True)
"""
"""
Questions for each of the exams.
@param id: the unique id corresponding to this particular question.
@param exam_id: the unique id corresponding to the exam.
@param question_text: the question (ex. What is the probability of getting 2 heads?)
"""
"""
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    question_text = db.Column(db.String)"""