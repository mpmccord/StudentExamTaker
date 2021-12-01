from . import db


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    course = db.Column(db.String, unique=False)
    teacher = db.Column(db.Integer)
    school = db.Column(db.String)