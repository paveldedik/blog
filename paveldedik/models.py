# -*- coding: utf-8 -*-


from datetime import datetime

from flask.ext.mongoengine.wtf import model_form
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from paveldedik import db


class User(db.Document):
    """Representation of an user."""

    #: User's email address. Reqired field.
    email = db.StringField(required=True)

    #: User's nick, 30 characters at most. Reqired field.
    username = db.StringField(max_length=30, required=True)

    #: User's password. Reqired field.
    password = db.StringField(max_length=100, required=True)

    #: User's first name, 50 characters at most.
    first_name = db.StringField(max_length=50)

    #: User's family name, 50 characters at most.
    last_name = db.StringField(max_length=50)

    def set_password(self, value):
        """Generates a password hash for the parameter `value` and sets
        the attribute ``password`` to the result.

        :param value: Unhashed password.
        :type value: string
        """
        self.password = generate_password_hash(value)

    def check_password(self, value):
        """Returns :obj:`True` if the given password matches for the
        encrypted attribute ``password``.

        :param value: Unhashed password.
        :type value: string
        """
        return check_password_hash(self.password, value)


UserForm = model_form(User)


class Post(db.Document):
    """Representation of an article."""

    #: Unique identification of the article, 50 characters at most.
    post_id = db.StringField(max_length=50)

    #: Title of the article, 120 characters at most. Required field.
    title = db.StringField(max_length=120, required=True)

    #: Leading paragraph of the articel. Required field.
    leading = db.StringField(required=True)

    #: Content of the article. Required field.
    content = db.StringField(required=True)

    #: Date and time when the article was published.
    published = db.DateTimeField(default=datetime.now(), required=True)

    #: Author of the article. Optional field.
    author = db.ReferenceField(User)

    #: List of tags, 30 characters at most for each tag. Optional field.
    tags = db.ListField(db.StringField(max_length=30))

    #: Register the index.
    meta = {
        'indexes': [
            {'fields': ['-post_id'], 'unique': True,
             'sparse': True, 'types': False},
        ],
    }


PostForm = model_form(Post)
