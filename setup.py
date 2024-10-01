#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='JackIt',
    version='2.0.0',
    author='doublesec',
    packages=['jackit', 'jackit.lib', 'jackit.plugins'],
    scripts=['bin/jackit'],
    url='https://github.com/doublesecc/jackit-python3',
    license='CC0-1.0 license',
    description='.',
    install_requires=[
        "click>=8.0",   # Latest version compatible with Python 3
        "pyusb>=1.2.1", # Latest version
        "six>=1.16.0"   # Latest version
    ],
)

