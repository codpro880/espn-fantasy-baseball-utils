# from distutils.core import setup
from setuptools import setup, find_packages


print find_packages()

setup(name='espn_fantasy_baseball',
      version='1.0',
      package_dir={'src': 'espn_fantasy_baseball'},
      packages=find_packages())
