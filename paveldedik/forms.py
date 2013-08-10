# -*- coding: utf-8 -*-


from flask.ext.mongoengine.wtf import model_form

from paveldedik.models import User, Post


post_args = {
    'title': {'label': u'Title'},
    'leading': {'label': u'Leading'},
    'content': {'label': u'Content'},
}


UserForm = model_form(User)

PostForm = model_form(Post, field_args=post_args)
