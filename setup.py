#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='nodebox-color',
    version='1.9.4.6-f2k',
    description='Color classes for python',
    long_description='Color classes for python, from the Nodebox project v1.0-series source.',
    author='Alexander Bohn',
    author_email='fish2000@gmail.com',
    url='http://github.com/fish2000/nodebox-color',
    download_url='https://github.com/fish2000/nodebox-color/archives/master',
    py_modules = [
        'colors',
    ],
    packages=[
        'colors',
    ],
    package_data={
        'colors': [
            'aggregated/adjectives/*.xml',
            'aggregated/basic_english/*.xml',
            'aggregated/emotion/*.xml',
            'aggregated/nature/*.xml',
            'context/*.txt',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)