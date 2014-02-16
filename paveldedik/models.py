# -*- coding: utf-8 -*-


from datetime import datetime

from flask.ext.login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from . import db
from .utils import slugify


class User(db.Document, UserMixin):
    """Representation of a User."""

    #: User's nick, 30 characters at most. Reqired field.
    username = db.StringField(primary_key=True, max_length=30)

    #: User's password. Reqired field.
    password = db.StringField(required=True, max_length=100)

    #: User's email address. Reqired field.
    email = db.StringField(required=True)

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

    @classmethod
    def find(cls, name):
        """Gets user by their username. Returns :obj:`None` if
        no such user exists.
        """
        return cls.objects.filter(username=name).first()

    @classmethod
    def authenticate(cls, form):
        """Gets the user's instance by username and checks
        their passowrd.

        :param form: Instance of :class:`~paveldedik.forms.LoginForm`.
        """
        user = cls.find(name=form.username.data)
        if user is not None:
            return user, user.check_password(form.password.data)
        else:
            return None, False


class Post(db.Document):
    """Representation of a Post."""

    #: Register the index.
    meta = {
        'ordering': ['-created_at']
    }

    #: Unique identification of the post.
    slug = db.StringField(primary_key=True)

    #: Title of the post, 120 characters at most. Required field.
    title = db.StringField(max_length=120, required=True)

    #: Leading paragraph of the articel. Required field.
    leading = db.StringField(required=True)

    #: Content of the post. Required field.
    content = db.StringField(required=True)

    #: Date and time when the post was published.
    published = db.DateTimeField(default=datetime.now, required=True)

    #: Author of the post. Optional field.
    author = db.ReferenceField(User)

    #: List of tags, 30 characters at most for each tag. Optional field.
    tags = db.ListField(db.StringField(max_length=30))

    @classmethod
    def from_form(cls, form):
        """Create instance of the post from the form."""
        slug = slugify(form.title.data)
        post = Post(pk=slug)
        form.populate_obj(post)
        return post
