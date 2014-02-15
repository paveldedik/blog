# -*- coding: utf-8 -*-


import jinja2
from datetime import date

from markdown import markdown

from .utils import slugify
from . import app, __author__ as author


@app.template_filter('html')
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


@app.template_filter('copyright')
def print_copyright(year):
    """Template filter that prints copyright.

    :type year: integer
    :rtype: :class:`jinja2.Markup` object
    """
    current_year = date.today().year
    if current_year == year:
        period = str(year)
    else:
        period = '{0}&ndash;{1}'.format(year, current_year)
    copyright = u'&copy; {}&nbsp;&nbsp;{}'
    return jinja2.Markup(copyright.format(period, author))


@app.template_filter('date')
def to_date(datum, format='%B %d, %Y'):
    """Template filter that prints given date.

    :type datum: datetime
    :param format: Format of the printed date.
    :type format: string
    :rtype: :class:`jinja2.Markup` object
    """
    return datum.strftime(format)


@app.template_filter('slug')
def create_slug(text):
    """Creates a slug from the given string. See
    :func:`~paveldedik.utils.slugify`.

    :type text: unicode
    :rtype: unicode
    """
    return slugify(text, length=None)
