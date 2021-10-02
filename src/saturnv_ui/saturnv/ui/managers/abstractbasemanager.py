from __future__ import annotations

import six
import abc

import typing


@six.add_metaclass(abc.ABCMeta)
class AbstractBaseManager(object):

    def __init__(self):
        self._sub_managers = {}
        self._items = {}

    def register_item(self, name: str, item: typing.Any):
        self.__setattr__(name, item)
        self._items[name] = item

    def register_sub_manager(self, submanager: AbstractBaseManager):
        self._sub_managers[submanager.name] = submanager
        self.__setattr__(submanager.name, submanager)

    def discover(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()

    def __iter__(self):
        yield from self.iter_managers()
        yield from self.iter_items()

    def iter_items(self) -> typing.Iterable[typing.Any]:
        for name, item in self._items.items():
            yield name, item

    def iter_managers(self) -> typing.Iterable[AbstractBaseManager]:
        for name, manager in self._sub_managers.items():
            yield name, manager
