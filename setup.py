from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "NAME",
    version = "0.1",
    packages = find_packages(),
    scripts = [],

    install_requires = ["nose"],

    #metadata
    author = "Nicholas Rutherford",
    author_email = "nicholas@isomorphism.ca",
    description = "?",
    license = "?",
    keywords = "?",
    url = "?",
)
