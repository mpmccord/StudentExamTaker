import flask_login


class User(flask_login.UserMixin):
    pass


class Teacher(User):
    pass
