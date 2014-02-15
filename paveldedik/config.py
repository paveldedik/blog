# -*- coding: utf-8 -*-


from . import app


#: Debug mode enabled by default.
DEBUG = True

#: Secret key in order to use sessions and CSRF validation.
SECRET_KEY = 'development key'

#: Enable or disable CSRF validation.
CSRF_ENABLED = True

#: Mongo database settings.
MONGODB_SETTINGS = {'DB': app.name}

#: Show line numbers in code block.
CODEHILITE_LINENUMS = False

#: Allow Pygments guess the language.
CODEHILITE_GUESS_LANG = False
