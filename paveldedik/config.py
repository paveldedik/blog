# -*- coding: utf-8 -*-


from paveldedik import app


#: Debug mode enabled by default.
DEBUG = True

#: Secret key set in order to use sessions and CSRF validation.
SECRET_KEY = 'development key'

#: Mongo database settings.
MONGODB_SETTINGS = {'DB': app.name}
