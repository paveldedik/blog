# -*- coding: utf-8 -*-


import re
from unicodedata import normalize

import jinja2
from markdown import markdown


_slug_regex = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def to_html(text):
    """Convert a markdown string to HTML and return HTML as a unicode string.

    :type text: string or unicode
    :rtype: :class:`jinja2.Markup` object
    """
    result = markdown(text, extensions=['codehilite'])
    return jinja2.Markup(result)


def slugify(text, delim=u'-', length=60):
    """Generates an ASCII-only slug. A slug is the part of a URL which
    identifies a page using human-readable keywords.

    :type text: unicode
    :param delim: Separator for white space characters. Default is hyphen.
    :type delim: unicode
    :param length: Maximum lenght of the result. Default is `60`.
    :type length: integer
    :rtype: unicode
    """
    result = []
    text = text[:length].lower()
    for word in _slug_regex.split(text):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))
