import abc
import uuid
import copy

from .field import Field

import typing


class ModelBase(object, metaclass=abc.ABCMeta):

    __fields__ = []

    id: uuid.UUID = Field()
    name: typing.AnyStr = Field()

    def __init__(self, name: typing.AnyStr, id: uuid.UUID = None):
        for field in self.__fields__:
            setattr(self, f'_{field.name}', None)

        self.id = id if id else uuid.uuid4()
        self.name = name

    @classmethod
    def from_dict(cls, dict_):

        dict_ = copy.copy(dict_)

        field_names = [f.name for f in cls.__fields__]
        for name in list(dict_.keys()):
            if name not in field_names:
                dict_.pop(name)

        return cls(**dict_)

    def to_dict(self):
        dict_ = {}
        for field_ in self.__fields__:
            dict_[field_.__name__] = getattr(self, field_.__name__)

        return dict_

    def update_from_dict(self, dict_):
        for key, value in dict_:
            setattr(self, key, value)
