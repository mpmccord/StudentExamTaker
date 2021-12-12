"""
This is a test to show how to add courses to users.
"""
from models import User, Course, db
user = User.query.filter_by(email="melanie.mccord19@ncf.edu").first()