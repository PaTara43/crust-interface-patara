#!/usr/bin/env python3

from logging import getLogger
from setuptools import setup

logger = getLogger(__name__)


# install yarn packages somehow

setup(name='crust-file-uploader',
      version='0.2.0',
      description='A simple python tool to upload files to Crust Network',
      author='Pavel Tarasov',
      author_email='p040399@outlook.com',
      url='https://github.com/PaTara43/crust-file-uploader',
      packages=['crust_file_uploader'],
      install_requires=['substrate-interface>=1.2.5,<2'],
      )
