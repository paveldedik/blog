# -*- coding: utf-8 -*-


from datetime import datetime
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from paveldedik import db


class User(db.Document):
    """Representation of a User."""

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


class Post(db.Document):
    """Representation of a Post."""

    #: Unique identification of the post, 50 characters at most.
    post_id = db.StringField(max_length=50, required=True)

    #: Title of the post, 120 characters at most. Required field.
    title = db.StringField(max_length=120, required=True)

    #: Leading paragraph of the articel. Required field.
    leading = db.StringField(required=True)

    #: Content of the post. Required field.
    content = db.StringField(required=True)

    #: Date and time when the post was published.
    published = db.DateTimeField(default=datetime.now(), required=True)

    #: Author of the post. Optional field.
    author = db.ReferenceField(User)

    #: List of tags, 30 characters at most for each tag. Optional field.
    tags = db.ListField(db.StringField(max_length=30))

    #: Register the index.
    meta = {
        'indexes': ['post_id'],
        'ordering': ['-created_at']
    }
