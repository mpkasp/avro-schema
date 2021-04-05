import os
import sys

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='avro-schema',
    version='0.3.3',
    author='Sam Mosleh',
    author_email='sam.mosleh@ut.ac.ir',
    packages=find_packages(),
    # include_package_data=True,
    install_requires=[
    ],
    description='',
    url='https://github.com/sam-mosleh/avro-schema',
    long_description=README,
    python_requires='>=3.8.5'
)
