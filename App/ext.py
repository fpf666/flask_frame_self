#封装扩展库

from flask_session import Session

from App.models import db


def init_app(app):
    db.init_app(app=app)
    Session(app=app)