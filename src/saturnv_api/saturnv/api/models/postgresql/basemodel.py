from __future__ import annotations

from sqlalchemy.orm.session import Session

from saturnv.api.models.base import AbstractBaseModel


class PostgresqlBaseModelMixin(AbstractBaseModel):

    __interface_class__ = None

    def __init__(self, interface=None, **kwargs):
        super().__init__(**kwargs)
        self._interface = interface if interface else self.__interface_class__()

    def set_attribute(self, name, value):
        setattr(self._interface, name, value)

    def get_attribute(self, name):
        return getattr(self._interface, name)

    def commit(self):
        self.session.commit()

    @property
    def metadata(self):
        return self.get_attribute('metadata_')

    @property
    def session(self):
        return Session.object_session(self._interface)

    def serialise(self):
        j = {}
        for column in self._interface.__table__.columns.keys():
            j[column] = getattr(self, column)
        return j
