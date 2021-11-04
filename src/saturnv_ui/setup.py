from setuptools import setup, find_namespace_packages

setup(
    name='saturnv_ui',
    packages=find_namespace_packages(include=['saturn.ui']),
    requires=[
        'libsass',
        'Qt.py',
        'PyQt5',
        'saturnv.api'
    ]
)
