#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '1.2'

setup(name='sip-proxpy',
      
      version=version,
      
      description="Customizable HTTP/HTTPS proxy with plugin architecture",
      
      long_description="""\
A fork of ProxPy as used in DAVID Social Innovation Platform""",
      
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      
      keywords='python proxy, proxpy, shiny-server-pro',
      
      author='Roberto Paleari, Allessandro Reina' ,
      author_email='roberto.paleari@gmail.com, allesandro.reina@gmail.com',
      
      maintainer='Frans van Dunné',
      maintainer_email='frans@southshield.net', 
      
      url='http://innovateonline.nl',
      
      license='GPLv3+',
      
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      sipproxpy = sipproxpy.proxpy:main
      """,
      )
