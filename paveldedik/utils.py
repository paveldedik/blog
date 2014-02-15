# -*- coding: utf-8 -*-


import re
from unicodedata import normalize

from flask.views import MethodView

from . import app


_slug_regex = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-', length=60):
    """Generates an ASCII-only slug. A slug is the part of a URL which
    identifies a page using human-readable keywords.
    See `Generating Slugs<http://flask.pocoo.org/snippets/5/>`_.

    :type text: unicode
    :param delim: Separator for white space characters. Default is hyphen.
    :type delim: unicode
    :param length: Maximum lenght of the result. Default is `60`.
    :type length: integer
    :rtype: unicode
    """
    result = []
    text = text if length is None else text[:length]
    for word in _slug_regex.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def underscore(string):
    """Converts input to under_scored string.

    :param string: Camel-case string to be converted.
    :return: Snake-case string.
    """
    string = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', string).lower()


class route(object):
    """Class decorator to simplify route registration."""

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def __call__(self, cls):
        assert issubclass(cls, MethodView)

        view_name = underscore(cls.__name__)
        app.add_url_rule(self.endpoint, view_func=cls.as_view(view_name))
        return cls
