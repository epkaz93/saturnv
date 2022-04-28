from __future__ import annotations

import enum

from .base import ModelBase
from .field import Field

import typing
if typing.TYPE_CHECKING:
    from typing import AnyStr


class ComparisonType(enum.Enum):

    and_ = 'and'
    or_ = 'or'
    greaterthanequals = '>='


class Package(ModelBase):

    version: AnyStr = Field()
    comparison: ComparisonType = Field()

    def __init__(self, name: AnyStr, version: AnyStr,
                 comparison: ComparisonType, id=None):
        super().__init__(name, id)
        self.version = version
        self.comparison = comparison

    @property
    def major(self):
        return self.version_parts[0]

    @property
    def minor(self):
        return self.version_parts[1]

    @property
    def patch(self):
        return self.version_parts[2]

    @property
    def version_parts(self):
        parts = []
        for part in self.version.split('.'):
            try:
                parts.append(int(part))
            except ValueError:
                parts.append(part)
        return parts
