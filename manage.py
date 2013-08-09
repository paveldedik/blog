#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paveldedik import app, db
from flask.ext.script import Manager


manager = Manager(app)


@manager.command
def dropdb():
    """Drops database."""
    db.connection.drop_database(app.name)
    print 'Database dropped.'


if __name__ == '__main__':
    manager.run()
