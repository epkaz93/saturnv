from saturnv.api.databases import postgresql as database
from saturnv.api.models import base

from .basemodel import PostgresqlBaseModelMixin
from .presets import PresetModel, VersionModel, ShortcutModel

import typing


class ShelfModel(PostgresqlBaseModelMixin, base.AbstractShelfModel):

    __interface_class__ = database.Shelf

    def __init__(self, interface: database.Shelf = None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        base.AbstractShelfModel.__init__(self, **kwargs)

    @property
    def presets(self) -> typing.List[PresetModel]:
        return [PresetModel(p) for p in self._interface.presets]

    @property
    def versions(self) -> typing.List[VersionModel]:
        return [VersionModel(v) for v in self._interface.versions]

    @property
    def shortcuts(self) -> typing.List[ShortcutModel]:
        return [ShortcutModel(s) for s in self._interface.shortcuts]
