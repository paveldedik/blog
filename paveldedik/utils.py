# -*- coding: utf-8 -*-


import re
from unicodedata import normalize


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
