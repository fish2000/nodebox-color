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
    zip_safe=False,
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
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Nodebox',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Public License v2',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)