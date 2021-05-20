from uuid import UUID

from sqlalchemy.orm import Session
from saturnv import model

from saturnv.repository.abstractrepository import AbstractRepository
from saturnv.repository.postgresql import orm


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session):
        super().__init__()
        orm.start_mappers()
        self.session = session

    def _add_preset(self, preset: model.Preset):
        self.session.add(preset)

    def _get_preset(self, uuid: UUID) -> model.Preset:
        return self.session.query(model.Preset).filter_by(uuid=uuid).first()

    def _add_shelf(self, shelf: model.Shelve):
        self.session.add(shelf)

    def _get_shelf(self, uuid: UUID) -> model.Shelve:
        return self.session.query(model.Shelve).filter_by(uuid=uuid).first()

    def _add_shortcut(self, shortcut: model.Shortcut):
        self.session.add(shortcut)

    def _get_shortcut(self, uuid: UUID) -> model.Shortcut:
        return self.session.query(model.Shortcut).filter_by(uuid=uuid).first()

    def _all_presets(self):
        return self.session.query(model.Preset).all()
