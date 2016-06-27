#
# Copyright 2012 John Keyes
#
# http://jkeyes.mit-license.org/
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="python-intercom",
    version='2.1.1.2',
    description="Intercom API wrapper",
    long_description=long_description,
    author="John Keyes",
    author_email="john@keyes.ie",
    license="MIT License",
    url="http://github.com/jkeyes/python-intercom",
    keywords='Intercom crm python',
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests", "inflection", "six"],
    zip_safe=False
)
