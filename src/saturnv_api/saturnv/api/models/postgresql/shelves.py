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

    def _get_links_by_type(self, type_):
        if type_ == 'preset':
            table = database.Preset
        elif type_ == 'version':
            table = database.Version
        elif type_ == 'shortcut':
            table = database.Shortcut
        else:
            raise ValueError(type_)
        links = self._interface.links.filter(database.ShelfLink.entity_type == type_).all()
        types = self.session.query(table).filter(
            table.uuid.in_([link.entity_uuid for link in links])
        ).all()
        return types

    @property
    def presets(self) -> typing.List[PresetModel]:
        return [PresetModel(p) for p in self._get_links_by_type('preset')]

    @property
    def versions(self) -> typing.List[VersionModel]:
        return [VersionModel(v) for v in self._get_links_by_type('version')]

    @property
    def shortcuts(self) -> typing.List[ShortcutModel]:
        return [ShortcutModel(s) for s in self._get_links_by_type('shortcut')]

    def _add_link(self, entity_type, entity_uuid):
        link = database.ShelfLink(shelf_uuid=self.uuid, entity_type=entity_type, entity_uuid=entity_uuid)
        self.session.add(link)
        self.commit()

    def _delete_link(self, entity_type, entity_uuid):
        self.session.query(database.ShelfLink).filter(
            database.ShelfLink.shelf_uuid == self.uuid,
            database.ShelfLink.entity_type == entity_type,
            database.ShelfLink.entity_uuid == entity_uuid
        ).delete()
        self.commit()
