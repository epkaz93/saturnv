from __future__ import annotations

import six
import abc

from . import AbstractBaseModel

import typing
if typing.TYPE_CHECKING:
    from . import AbstractPresetModel, AbstractVersionModel, AbstractShortcutModel


@six.add_metaclass(abc.ABCMeta)
class AbstractShelfModel(AbstractBaseModel):

    @property
    def name(self):
        return self.get_attribute('name')

    @property
    def author(self):
        return self.get_attribute('author')

    @property
    def path(self):
        return self.get_attribute('path')

    @property
    @abc.abstractmethod
    def presets(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def versions(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def shortcuts(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _add_link(self, entity_type, entity_uuid):
        raise NotImplementedError

    @abc.abstractmethod
    def _delete_link(self, entity_type, entity_uuid):
        raise NotImplementedError

    def add_preset(self, preset: AbstractPresetModel):
        self._add_link('preset', preset.uuid)

    def add_version(self, version: AbstractVersionModel):
        self._add_link('version', version.uuid)

    def add_shortcut(self, shortcut: AbstractShortcutModel):
        self._add_link('shortcut', shortcut.uuid)

    def remove_preset(self, preset: AbstractPresetModel):
        self._delete_link('preset', preset.uuid)

    def remove_version(self, version: AbstractVersionModel):
        self._delete_link('version', version.uuid)

    def remove_shortcut(self, shortcut: AbstractShortcutModel):
        self._delete_link('shortcut', shortcut.uuid)
