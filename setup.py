# _*_ encoding: utf-8 _*_

from setuptools import setup

NAME = 'calculator'
VERSION = '0.1.0'
AUTHOR = 'Fernando Ferreira'
AUTHOR_EMAIL = 'fernando.ferreira.tbe@gmail.com'
DESCRIPTION = 'Calculator app'
LONG_DESCRIPTION = 'Calculator app created to test install_requirements feature from python setup'
LICENSE = 'MIT'
URL = 'www.example.com'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    license=LICENSE,
    package=[
        'calculator',
        'calculator.test'
    ],
    install_requires=['wheel', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
