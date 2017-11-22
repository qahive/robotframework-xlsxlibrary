# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="robotframework-xlsxlibrary",
    version="0.1.0",
    description="A robotframework library for read and write execel file",
    license="MIT",
    author="Atthaboon Sanurt",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
