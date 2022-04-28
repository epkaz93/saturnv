from __future__ import annotations

import getpass

from .base import ModelBase
from .field import Field

import typing
if typing.TYPE_CHECKING:
    from typing import AnyStr
    from .package import Package
    from .resource import ResourceType

    PackagesList = typing.List[Package]
    ResourcesList = typing.List[ResourceType]


class Preset(ModelBase):

    author: AnyStr = Field()
    packages: PackagesList = Field()
    commands: typing.List = Field()
    environment_variables: typing.Dict = Field()

    metadata: typing.Dict = Field()
    resources: ResourcesList = Field()

    def __init__(self, name: AnyStr, author: AnyStr = None, packages: PackagesList = None,
                 commands=None, environment_variables=None, resources: ResourcesList = None,
                 metadata=None, id=None):
        super().__init__(name, id)

        self.author = author if author else getpass.getuser()
        self.packages = packages if packages else []
        self.commands = commands if commands else []
        self.environment_variables = environment_variables if environment_variables else {}
        self.metadata = metadata if metadata else {}
        self.resources = resources if resources else []
