#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='JackIt',
    version='0.1.0',
    author='infamy and phikshun',
    packages=['jackit', 'jackit.lib', 'jackit.plugins'],
    scripts=['bin/jackit'],
    url='https://github.com/insecurityofthings/jackit',
    license='BSD',
    description='.',
    install_requires=[
        "click>=8.0",   # Latest version compatible with Python 3
        "pyusb>=1.2.1", # Latest version
        "tabulate", # Latest version
        "six>=1.16.0"   # Latest version
    ],
)

