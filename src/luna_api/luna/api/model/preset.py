import uuid

from .base import ModelBase
from .field import Field

from .resource import ResourceType
from .package import PackageType

import typing


class Preset(ModelBase):

    packages = Field()
    commands = Field()
    metadata = Field()
    resources = Field()

    def __init__(self, name, packages=None, commands=None, environment_variables=None,
                 resources=None, metadata=None, id=None):
        super().__init__(name, id)


'''
@dataclass
class _Preset(object):

    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    packages: typing.List[PackageType] = field(default_factory=lambda: [])
    commands: typing.List = field(default_factory=lambda: [])
    metadata: typing.List = field(default_factory=lambda: [])
    resources: typing.List[ResourceType] = field(default_factory=lambda: [])

    @classmethod
    def from_dict(cls, dict_):
        return cls(name=dict_['name'])
'''
'''

class Preset(ModelBase):



        super().__init__(name, id)
        self.packages = packages if packages else []
        self.commands = commands if commands else []
        self.environment_variables = environment_variables if environment_variables else []
        self.resources = resources if resources else []
        self.metadata = metadata if metadata else {}

    @field
    def packages(self):
        return self._packages

    @packages.setter
    def packages(self, packages):
        self._packages = packages

    @field
    def commands(self):
        return self._commands

    @commands.setter
    def commands(self, commands):
        self._commands = commands

    @field
    def environment_variables(self):
        return self._commands

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        self._environment_variables = environment_variables

    @field
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, resources):
        self._resources = resources

    @field
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        self._metadata = metadata
'''