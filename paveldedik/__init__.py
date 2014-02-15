# -*- coding: utf-8 -*-

__author__ = 'Pavel Dedik'
__version__ = '0.1'


from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('paveldedik.config')

db = MongoEngine(app)


import paveldedik.views  # noqa
import paveldedik.filters  # noqa
