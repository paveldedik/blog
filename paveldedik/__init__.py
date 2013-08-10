# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('paveldedik.config')

db = MongoEngine(app)


from paveldedik import views
