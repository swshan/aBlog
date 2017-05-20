#coding=utf-8
import os

from flask import Flask
from blog.views import bp_views
from blog.db import *

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_views)

    return app

app = create_app()

# some vars
basedir = os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.run(host='127.0.0.1', port=5000)