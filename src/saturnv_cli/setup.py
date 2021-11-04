from setuptools import setup, find_namespace_packages

setup(
    name='saturnv_cli',
    packages=find_namespace_packages(include=['saturn.cli'])
)
