from werkzeug.security import generate_password_hash

from app import *

app = create_app()


@app.before_first_request
def createDatabase():
    db.create_all()
    new_user = User(email="test@example.com", password=generate_password_hash("secret", method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()


if __name__ == '__main__':
    app.run(port=5685)
