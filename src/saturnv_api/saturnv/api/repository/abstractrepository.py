from __future__ import annotations

import abc
from uuid import UUID

import typing

if typing.TYPE_CHECKING:
    from src import model


class AbstractRepository(abc.ABC):

    def __init__(self):
        pass

    @classmethod
    @abc.abstractmethod
    def create_repository(cls):
        raise NotImplementedError

    def add_preset(self, preset: model.Preset):
        self._add_preset(preset)
        preset.associate_repository(self)
        self.commit()

    def get_preset(self, uuid: UUID) -> model.Preset:
        preset = self._get_preset(uuid)
        preset.associate_repository(self)
        return preset

    def add_version(self, version: model.Version):
        self._add_version(version)
        version.associate_repository(self)
        self.commit()

    def get_version(self, uuid: UUID) -> model.Version:
        version = self._get_version(uuid)
        version.associate_repository(self)
        return version

    def add_setting(self, setting: model.Setting):
        self._add_setting(setting)
        setting.associate_repository(self)
        self.commit()

    def get_setting(self, uuid: UUID) -> model.Setting:
        setting = self._get_setting(uuid)
        setting.associate_repository(self)
        return setting

    def add_shelf(self, shelf: model.Shelf):
        self._add_shelf(shelf)
        self.commit()

    def get_shelf(self, uuid: UUID) -> model.Shelf:
        return self._get_shelf(uuid)

    def add_shortcut(self, shortcut: model.Shortcut):
        self._add_shortcut(shortcut)
        self.commit()

    def get_shortcut(self, uuid: UUID) -> model.Shortcut:
        return self._get_shortcut(uuid)

    def all_presets(self):
        presets = self._all_presets()
        for preset in presets:
            preset.associate_repository(self)
        return self._all_presets()

    def all_shelves(self):
        return self._all_shelves()

    def versions_from_preset(self, preset: model.Preset):
        return self._versions_from_preset(preset)

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _add_preset(self, preset: model.Preset):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_preset(self, uuid: UUID) -> model.Preset:
        raise NotImplementedError

    @abc.abstractmethod
    def _add_version(self, version: model.Version):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_version(self, uuid: UUID) -> model.Version:
        raise NotImplementedError

    @abc.abstractmethod
    def _add_setting(self, version: model.Setting):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_setting(self, uuid: UUID) -> model.Setting:
        raise NotImplementedError

    @abc.abstractmethod
    def _add_shelf(self, shelf: model.Shelf):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_shelf(self, uuid: UUID) -> model.Shelf:
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

    @abc.abstractmethod
    def _all_shelves(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _versions_from_preset(self, preset: model.Preset):
        raise NotImplementedError
