from __future__ import print_function
from exam_backend.login import *

from exam_backend import models
from exam_backend.models import User, db, Course
from exam_backend import create_app
from flask_migrate import Migrate
import sys

app = create_app()
db.init_app(app)
app.app_context().push()
db.create_all()

migrate = Migrate(app, db)
users = User.query.all()
print("Users", users, file = sys.stderr)
@app.before_first_request
def createDatabase():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5685, debug=True)
