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
    courses = db.relationship("Course", backref="course_teacher", lazy = True)
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
    exams = db.relationship("Exam", backref="course_for_exam")

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String, unique = True)
    course_class = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    school = db.Column(db.String)