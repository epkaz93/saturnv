from luna.plugin.baseplugin import PluginBase
import luna.api

from yaml_datasource.api import repository
from yaml_datasource.api import query

import typing


class YamlDatasourcePlugin(PluginBase):

    @property
    def name(self) -> typing.AnyStr:
        return 'yaml_api_plugin'

    @property
    def long_name(self) -> typing.AnyStr:
        return 'Yaml API Repository Plugin'

    @property
    def description(self) -> typing.AnyStr:
        return """"""

    @property
    def version(self) -> typing.AnyStr:
        return '0.0.1'

    @property
    def type(self) -> typing.AnyStr:
        return 'api'

    @property
    def author(self) -> typing.AnyStr:
        return 'thomaswilmot@gmail.com'

    @classmethod
    def _load(cls):
        luna.api.repository.yaml = repository
        luna.api.query.yaml = query
