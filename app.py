from werkzeug.security import generate_password_hash

from exam_backend import my_user_accounts
from exam_backend.my_user_accounts import User
from exam_backend.my_user_accounts import db
from exam_backend import create_app

app = create_app()
db.init_app(app)
@app.before_first_request
def createDatabase():
    db.create_all()
    """
    new_user = User(email="foo.bar@example.com", password=generate_password_hash("secret", method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    """

if __name__ == '__main__':
    app.run(port=5685)
