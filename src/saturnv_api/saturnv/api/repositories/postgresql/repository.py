from sqlalchemy.orm.session import Session

from saturnv.api.repositories.base import AbstractRepository
from saturnv.api.databases.postgresql import Preset, Shelf
from saturnv.api.models.postgresql import PresetModel, ShelfModel

import typing


class Repository(AbstractRepository):

    def __init__(self, session: Session):
        super().__init__(session)

    def get_presets(self, deleted=False) -> typing.List[PresetModel]:
        query = self._session.query(Preset)
        return [PresetModel(interface=p) for p in query.filter(Preset.deleted == deleted).all()]

    def get_shelves(self, deleted=False) -> typing.List[ShelfModel]:
        query = self._session.query(Shelf)
        return [ShelfModel(interface=s) for s in query.all()]

    def commit(self):
        return self._session.commit()
