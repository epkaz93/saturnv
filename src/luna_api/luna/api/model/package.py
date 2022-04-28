import enum
from dataclasses import dataclass

import typing


class ComparisonType(enum.Enum):

    and_ = 'and'
    or_ = 'or'
    greaterthanequals = '>='


@dataclass
class Package(object):

    name: typing.AnyStr
    version: typing.AnyStr = ''
    comparison: typing.AnyStr = ComparisonType.greaterthanequals

    @property
    def major(self):
        return self.version_parts[0]

    @property
    def version_parts(self):
        parts = []
        for part in self.version.split('.'):
            try:
                parts.append(int(part))
            except ValueError:
                parts.append(part)
        return parts


PackageType = typing.TypeVar('PackageType', bound=Package)
