# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='thesaurus-cli',
    version='1.0.1',
    description='A command line interface for Thesaurus.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davidgu/thesaurus-cli',
    author='David Gu',
    py_modules=["thesaurus"],
    install_requires=['beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'thesaurus=thesaurus:main',
        ],
    },
)
