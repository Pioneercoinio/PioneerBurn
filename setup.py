#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='PioneerBurn',
      version='1.0',
      description='Validate and generate Pioneer coin burn notices',
      author='frods',
      author_email='frods@hotmail.com',
      url='https://github.com/Pioneercoinio/PioneerBurn',
      packages=['pioneer_burn'],
      package_dir={'pioneer_burn': '.'},
      install_requires=['jsonschema'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"]
)