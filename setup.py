#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-sdk',
    version='0.2.0',
    description='This client library is designed to support the Facebook '
                'Graph API and the official Facebook JavaScript SDK, which '
                'is the canonical way to implement Facebook authentication.',
    author='Facebook',
    url='http://github.com/pythonforfacebook/facebook-sdk',
    py_modules=[
        'facebook',
    ],
)
