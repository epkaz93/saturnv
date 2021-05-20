from sqlalchemy.orm import mapper

from saturnv import model
from saturnv import database


def start_mappers():
    mapper(model.Preset, database.Preset)
    mapper(model.Shelve, database.Shelf)
    mapper(model.Version, database.Version)
    mapper(model.Setting, database.Setting)
    mapper(model.Shortcut, database.Shortcut)
    mapper(model.Override, database.Override)
