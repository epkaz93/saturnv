from __future__ import annotations

import functools
import warnings

from sqlalchemy import func

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
    @functools.lru_cache()
    def latest_version(self) -> VersionModel:
        return VersionModel(interface=self._interface.versions.order_by(database.Version.creation_date.desc()).one())

    @property
    @functools.lru_cache()
    def version_count(self) -> int:
        return self.session.query(func.count(database.Version.uuid)).filter(database.Version.preset_uuid == self.uuid).count()


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
        settings = []

        for s in self._interface.settings:
            try:
                type_ = SettingModel.Types(s.type)
            except ValueError:
                type_ = None

            if type_ == SettingModel.Types.package:
                setting = PackageSettingModel(interface=s)
            elif type_ == SettingModel.Types.envvar:
                setting = EnvironmentVariableSettingModel(interface=s)
            elif type_ == SettingModel.Types.command:
                setting = CommandSettingModel(interface=s)
            else:
                setting = SettingModel(interface=s)

            settings.append(setting)

        return settings

    @property
    def shortcuts(self) -> typing.List[ShortcutModel]:
        return [ShortcutModel(interface=s) for s in self._interface.shortcuts]


class SettingModel(PostgresqlBaseModelMixin, base.AbstractSettingModel):

    __interface_class__ = database.Setting

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface=interface)
        base.AbstractSettingModel.__init__(self, **kwargs)

    @property
    def version(self) -> VersionModel:
        return VersionModel(interface=self._interface.version)


class PackageSettingModel(SettingModel, base.AbstractPackageSettingModel):

    def __init__(self, interface=None, **kwargs):
        if interface is not None:
            package = kwargs.get('package')
            kwargs['package'] = package if package else interface.name
            version = kwargs.get('version')
            kwargs['version'] = version if version else '.'.join(interface.value.get('version', []))
            comparison = kwargs.get('comparison')
            kwargs['comparison'] = comparison if comparison else interface.value.get('comparison', self.Comparisons.equals)

        PostgresqlBaseModelMixin.__init__(self, interface=interface)
        base.AbstractPackageSettingModel.__init__(self, **kwargs)


class EnvironmentVariableSettingModel(SettingModel, base.AbstractEnvironmentVariableSettingModel):

    def __init__(self, interface=None, **kwargs):
        SettingModel.__init__(self, interface)
        base.AbstractEnvironmentVariableSettingModel.__init__(self, **kwargs)


class CommandSettingModel(SettingModel, base.AbstractCommandSettingModel):

    def __init__(self, interface=None, **kwargs):
        if interface is not None:
            alias = kwargs.get('alias')
            kwargs['alias'] = alias if alias else interface.value.get('alias')
            command = kwargs.get('command')
            kwargs['command'] = command if command else interface.value.get('command')

        SettingModel.__init__(self, interface)
        base.AbstractCommandSettingModel.__init__(self, **kwargs)


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
