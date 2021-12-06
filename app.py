<<<<<<< HEAD
import flask
from flask import Flask, render_template, request
import flask_login
import os
from login import *
=======
from werkzeug.security import generate_password_hash
>>>>>>> d46189be77e12f55e974ca9ee75dc02e0c930b08

from exam_backend import models
from exam_backend.models import User
from exam_backend.models import db
from exam_backend import create_app
from flask_migrate import Migrate

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def createDatabase():
    db.create_all()
    """
    new_user = User(email="foo.bar@my_email.com", password=generate_password_hash("secret", method='sha256'), school = "University of South Florida", type_account = "Teacher")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    """

if __name__ == '__main__':
    app.run(port=5685, debug=True)
