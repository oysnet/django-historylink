#!/usr/bin/env python
from setuptools import setup, find_packages

import historylink

CLASSIFIERS = [
    'Intended Audience :: Developers',    
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python'    
]

KEYWORDS = 'django url change redirect 404 301'


setup(name = 'historylink',
    version = historylink.__version__,
    description = """Store model url change, od a permanent redirect on 404""",
    author = historylink.__author__,
    url = "https://github.com/oxys-net/django-historylink",
    packages = find_packages(),
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    zip_safe = True
)