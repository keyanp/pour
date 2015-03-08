#!/usr/bin/env python

from setuptools import setup

setup(
    name='pour',
    version='0.1',
    url='http://www.github.com/keyanp/pour',
    license='MIT',
    author='Keyan Pishdadian',
    author_email='kpishdadian@gmail.com',
    description='A lightweight Flask app generator.',
    entry_points={
        'console_scripts': ['pour']
    }

)
