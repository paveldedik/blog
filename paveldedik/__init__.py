# -*- coding: utf-8 -*-

__author__ = 'Pavel Dedik'
__version__ = '0.1'


from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine


### App setup

app = Flask(__name__)
app.config.from_object('paveldedik.config')


### DB setup

db = MongoEngine(app)


### User management

login_manager = LoginManager(app)

from .models import User

login_manager.login_view = 'login'
login_manager.user_callback = User.find


import paveldedik.views  # noqa
import paveldedik.filters  # noqa
