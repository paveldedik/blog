# -*- coding: utf-8 -*-


import re
from setuptools import setup, find_packages


# determine version
code = open('paveldedik/__init__.py', 'r').read(1000)
version = re.search(r'__version__ = \'([^\']*)\'', code).group(1)
author = re.search(r'__author__ = \'([^\']*)\'', code).group(1)


# read requirements
lines = open('requirements.txt').read().splitlines()
install_requires = filter(None, [line.split('#')[0].strip() for line in lines])


setup(
    name='paveldedik',
    version=version,
    author=author,
    py_modules=['manage'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_requires,
)
