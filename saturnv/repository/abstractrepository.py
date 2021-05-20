from __future__ import annotations

import abc
from uuid import UUID

import typing

if typing.TYPE_CHECKING:
    from saturnv import model


class AbstractRepository(abc.ABC):

    def __init__(self):
        pass

    def add_preset(self, preset: model.Preset):
        self._add_preset(preset)

    def get_preset(self, uuid: UUID) -> model.Preset:
        return self._get_preset(uuid)

    def add_shelf(self, shelf: model.Shelve):
        self._add_shelf(shelf)

    def get_shelf(self, uuid: UUID) -> model.Shelve:
        return self._get_shelf(uuid)

    def add_shortcut(self, shortcut: model.Shortcut):
        self._add_shortcut(shortcut)

    def get_shortcut(self, uuid: UUID) -> model.Shortcut:
        return self._get_shortcut(uuid)

    def all_presets(self):
        return self._all_presets()

    @abc.abstractmethod
    def _add_preset(self, preset: model.Preset):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_preset(self, uuid: UUID) -> model.Preset:
        raise NotImplementedError

    @abc.abstractmethod
    def _add_shelf(self, shelf: model.Shelve):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_shelf(self, uuid: UUID) -> model.Shelve:
        raise NotImplementedError

    @abc.abstractmethod
    def _add_shortcut(self, shortcut: model.Shortcut):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_shortcut(self, uuid: UUID) -> model.Shortcut:
        raise NotImplementedError

    @abc.abstractmethod
    def _all_presets(self):
        raise NotImplementedError