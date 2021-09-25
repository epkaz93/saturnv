from saturnv.api import database
from saturnv.api.model import base


from .basemodel import PostgresqlBaseModelMixin


class PresetModel(PostgresqlBaseModelMixin, base.AbstractPresetModel):

    __interface_class__ = database.Preset

    def __init__(self, interface: database.Preset = None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)

    @property
    def versions(self):
        return [VersionModel(interface=v) for v in self._interface.versions]


class VersionModel(PostgresqlBaseModelMixin, base.AbstractVersionModel):

    __interface_class__ = database.Version

    def __init__(self, interface: database.Version = None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)

    @property
    def preset(self):
        return PresetModel(interface=self._interface.preset)

    @property
    def settings(self):
        return [SettingModel(interface=s) for s in self._interface.settings]

    @property
    def shortcuts(self):
        return [ShortcutModel(interface=s) for s in self._interface.shortcuts]


class SettingModel(PostgresqlBaseModelMixin, base.AbstractSettingModel):

    __interface_class__ = database.Setting

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)

    @property
    def version(self):
        return VersionModel(interface=self._interface.version)


class ShortcutModel(PostgresqlBaseModelMixin, base.AbstractShortcutModel):

    __interface_class__ = database.Shortcut

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)

    @property
    def version(self):
        return VersionModel(interface=self._interface.version)


class OverrideModel(PostgresqlBaseModelMixin, base.AbstractOverrideModel):

    __interface_class__ = database.Override

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)

    @property
    def shortcut(self):
        return ShortcutModel(interface=self._interface.shortcut)
