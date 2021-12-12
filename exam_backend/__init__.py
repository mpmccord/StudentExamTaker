# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .login import login_stuff
from .models import User, db, Course
# init SQLAlchemy so we can use it later in our models
app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = os.urandom(256)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    lm = LoginManager()
    lm.login_view = 'auth.login'
    lm.init_app(app)

    @lm.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our exam_backend
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, name="auth")

    # blueprint for non-auth parts of exam_backend
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, name="main")

    app.register_blueprint(login_stuff, name="login_stuff")
    return app
