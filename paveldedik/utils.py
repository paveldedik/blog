# -*- coding: utf-8 -*-


import re
import jinja2
from unicodedata import normalize
from markdown import markdown

from paveldedik import app


_slug_regex = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def to_html(text):
    """Converts a markdown string to a HTML document. Uses the `CodeHilite
    <http://pythonhosted.org/Markdown/extensions/code_hilite.html>`_
    extension.

    :type text: string or unicode
    :rtype: :class:`jinja2.Markup` object
    """
    codehilite = 'codehilite(linenums={0}, guess_lang={1})'.format(
        app.config['CODEHILITE_LINENUMS'],
        app.config['CODEHILITE_GUESS_LANG'])
    result = markdown(text, extensions=[codehilite])
    return jinja2.Markup(result)


#: Put the :func:`to_html` in jinja2 filters.
app.jinja_env.filters['html'] = to_html


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
    text = text[:length].lower()
    for word in _slug_regex.split(text):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))
