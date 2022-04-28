from __future__ import annotations

import getpass

from .base import ModelBase
from .field import Field

import typing
if typing.TYPE_CHECKING:
    from typing import AnyStr
    from .resource import ResourceType

    ResourcesList = typing.List[ResourceType]


class Shelf(ModelBase):

    path: AnyStr = Field()
    author: AnyStr = Field()
    shortcuts: typing.List = Field()

    metadata: typing.Dict = Field()
    resources: ResourcesList = Field()

    def __init__(self, name: AnyStr, path: AnyStr, author: AnyStr=None,
                 shortcuts: typing.List = None, metadata: typing.Dict = None,
                 resources: ResourcesList = None, id=None):
        super().__init__(name, id)
        self.path = path
        self.author = author if author else getpass.getuser()
        self.shortcuts = shortcuts
        self.metadata = metadata
        self.resources = resources
