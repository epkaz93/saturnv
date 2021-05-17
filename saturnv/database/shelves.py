import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.mutable import MutableDict

from saturnv.database.core import Base


class Shelf(Base):

    __tablename__ = 'shelves'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    author = Column(String)
    path = Column(String)
    metadata_ = Column(MutableDict.as_mutable(JSONB), name='metadata')

    versions = relationship('Version', secondary='ShelfVersionLink')
