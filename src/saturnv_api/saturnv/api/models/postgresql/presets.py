from __future__ import annotations

from saturnv.api.databases import postgresql as database
from saturnv.api.models import base

from .basemodel import PostgresqlBaseModelMixin


import typing


class PresetModel(PostgresqlBaseModelMixin, base.AbstractPresetModel):

    __interface_class__ = database.Preset

    def __init__(self, interface: database.Preset = None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractPresetModel.__init__(self, **kwargs)

    @property
    def versions(self) -> typing.List[VersionModel]:
        return [VersionModel(interface=v) for v in self._interface.versions]

    @property
    def latest_version(self):
        return VersionModel(interface=self._interface.versions.order_by(database.Version.creation_date.desc()).one())


class VersionModel(PostgresqlBaseModelMixin, base.AbstractVersionModel):

    __interface_class__ = database.Version

    def __init__(self, interface: database.Version = None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractVersionModel.__init__(self, **kwargs)

    @property
    def preset(self) -> PresetModel:
        return PresetModel(interface=self._interface.preset)

    @property
    def settings(self) -> typing.List[SettingModel]:
        return [SettingModel(interface=s) for s in self._interface.settings]

    @property
    def shortcuts(self):
        return [ShortcutModel(interface=s) for s in self._interface.shortcuts]


class SettingModel(PostgresqlBaseModelMixin, base.AbstractSettingModel):

    __interface_class__ = database.Setting

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractSettingModel.__init__(self, **kwargs)

    @property
    def version(self) -> VersionModel:
        return VersionModel(interface=self._interface.version)


class ShortcutModel(PostgresqlBaseModelMixin, base.AbstractShortcutModel):

    __interface_class__ = database.Shortcut

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractShortcutModel.__init__(self, **kwargs)

    @property
    def version(self) -> VersionModel:
        return VersionModel(interface=self._interface.version)


class OverrideModel(PostgresqlBaseModelMixin, base.AbstractOverrideModel):

    __interface_class__ = database.Override

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractOverrideModel.__init__(self, **kwargs)

    @property
    def shortcut(self) -> ShortcutModel:
        return ShortcutModel(interface=self._interface.shortcut)
