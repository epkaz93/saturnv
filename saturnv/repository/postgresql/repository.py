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

    @classmethod
    def create_repository(cls):
        return cls(Session())

    def commit(self):
        self.session.commit()

    def _add_preset(self, preset: model.Preset):
        self.session.add(preset)

    def _get_preset(self, uuid: UUID) -> model.Preset:
        return self.session.query(model.Preset).filter_by(uuid=uuid).first()

    def _add_version(self, version: model.Version):
        self.session.add(version)

    def _get_version(self, uuid: UUID) -> model.Version:
        return self.session.query(model.Version).filter_by(uuid=uuid).first()

    def _add_setting(self, setting: model.Setting):
        self.session.add(setting)

    def _get_setting(self, uuid: UUID) -> model.Setting:
        return self.session.query(model.Setting).filter_by(uuid=uuid).first()

    def _add_shelf(self, shelf: model.Shelf):
        self.session.add(shelf)

    def _get_shelf(self, uuid: UUID) -> model.Shelf:
        return self.session.query(model.Shelf).filter_by(uuid=uuid).first()

    def _add_shortcut(self, shortcut: model.Shortcut):
        self.session.add(shortcut)

    def _get_shortcut(self, uuid: UUID) -> model.Shortcut:
        return self.session.query(model.Shortcut).filter_by(uuid=uuid).first()

    def _all_presets(self):
        return self.session.query(model.Preset).all()

    def _all_shelves(self):
        return self.session.query(model.Shelf).all()

    def _versions_from_preset(self, preset: model.Preset):
        versions = self.session.query(model.Version).filter_by(preset_uuid=preset.uuid).all()
        return versions
