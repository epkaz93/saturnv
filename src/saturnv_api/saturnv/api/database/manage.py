from saturnv.api.database.core import Base, Session
from saturnv.api.database import Preset, Version, Setting, Shortcut, Override, Shelf


def create_tables():
    session = Session()
    Base.metadata.create_all()
    session.commit()
