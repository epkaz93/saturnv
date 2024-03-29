from setuptools import setup, find_namespace_packages

setup(
    name='saturnv_api',
    packages=find_namespace_packages(include=['saturnv.api']),
    requires=[
        'six',
        'SQLAlchemy',
        'psycopg2',
        'psutil',
        'rez'
    ]
)
