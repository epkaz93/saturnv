import io
import abc
import uuid
from dataclasses import dataclass, field
import typing

from pathlib import Path


class _ResourceMeta(type):

    __type__ = None

    resource_interfaces = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        mcs.resource_interfaces[cls.__type__] = cls
        return cls

    @classmethod
    def create_resource(mcs, name, uri, type_):
        cls = mcs.resource_interfaces[type_]
        return cls(name=name, uri=uri)


class ResourceMeta(abc.ABCMeta, _ResourceMeta):

    pass


@dataclass
class ResourceBase(object, metaclass=abc.ABCMeta):

    __type__ = None

    name: typing.AnyStr
    uri: typing.AnyStr
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def get(self):
        """"""


class FilesystemResource(ResourceBase, metaclass=ResourceMeta):

    __type__ = 'filesystem'

    @property
    def path(self) -> Path:
        return Path(self.uri)

    @path.setter
    def path(self, path: Path):
        self.uri = str(path)

    def get(self):
        with io.open(self.uri) as f:
            return f.read()


ResourceType = typing.TypeVar('ResourceType', bound=ResourceBase)
