import uuid

from .base import ModelBase
from .field import Field

from .resource import ResourceType
from .package import PackageType

import typing


class Preset(ModelBase):

    packages = Field()
    commands = Field()
    environment_variables = Field()
    metadata = Field()
    resources = Field()

    def __init__(self, name, packages=None, commands=None, environment_variables=None,
                 resources=None, metadata=None, id=None):
        super().__init__(name, id)

        self.packages = packages
        self.commands = commands
        self.environment_variables = environment_variables
        self.metadata = metadata
        self.resources = resources
