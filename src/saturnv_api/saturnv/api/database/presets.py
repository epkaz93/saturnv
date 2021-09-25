import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.mutable import MutableDict

from saturnv.api.database.core import Base


class Preset(Base):

    __tablename__ = 'presets'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creation_date = Column(DateTime, default=datetime.now, nullable=False)
    author = Column(String, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
    metadata_ = Column(MutableDict.as_mutable(JSONB), name='metadata')

    versions = relationship('Version', backref=backref("preset", cascade='all, delete-orphan'))


class Version(Base):

    __tablename__ = 'versions'

    uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False, primary_key=True)
    icon = Column(String)
    description = Column(String)
    preset_uuid = Column(UUID(as_uuid=True), ForeignKey('presets.uuid'))
    creation_date = Column(DateTime, default=datetime.now, nullable=False)
    blame = Column(String, nullable=False)
    metadata_ = Column(MutableDict.as_mutable(JSONB), name='metadata')

    settings = relationship('Setting', backref="version", lazy='dynamic')
    shortcuts = relationship('Shortcut', backref="version", lazy='dynamic')


class AbstractValueBase(Base):

    __abstract__ = True

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String)
    name = Column(String)
    icon = Column(String)
    value = Column(MutableDict.as_mutable(JSONB))

    metadata_ = Column(MutableDict.as_mutable(JSONB), name='metadata')


class Setting(AbstractValueBase):

    __tablename__ = 'settings'

    version_uuid = Column(UUID(as_uuid=True), ForeignKey('versions.uuid'))


class Shortcut(Base):

    __tablename__ = 'shortcuts'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version_uuid = Column(UUID(as_uuid=True), ForeignKey('versions.uuid'))
    icon = Column(String)
    creation_date = Column(DateTime, default=datetime.now, nullable=False)
    author = Column(String, nullable=False)

    overrides = relationship('Override', backref='shortcut')

    metadata_ = Column(MutableDict.as_mutable(JSONB), name='metadata')


class Override(AbstractValueBase):

    __tablename__ = 'overrides'

    shortcut_uuid = Column(UUID(as_uuid=True), ForeignKey('shortcuts.uuid'))
