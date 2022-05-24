from setuptools import setup

setup(
    name='yaml_datasource',
    group='luna.plugins',
    entry_points={
        'luna.api.plugins': [
            'YamlDatasource = yaml_datasource.api.plugin:YamlDatasourcePlugin'
        ],
        'luna.ui.plugins': [
            'YamlUIDatasource = yaml_datasource.ui.plugin:YamlUIDatasourcePlugin'
        ]
    },
    requires=[
        'luna.api',
        'PyYaml',
    ]
)
