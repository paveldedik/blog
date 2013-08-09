# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.mongoengine import MongoEngine

from paveldedik.utils import to_html


app = Flask(__name__)
app.config.from_object('paveldedik.config')

app.jinja_env.filters['html'] = to_html

db = MongoEngine(app)


from paveldedik import views
