from __future__ import annotations

from saturnv.api.models.base import AbstractBaseModel

import typing
if typing.TYPE_CHECKING:
    from sqlalchemy.orm.session import Session


class PostgresqlBaseModelMixin(AbstractBaseModel):

    __interface_class__ = None

    def __init__(self, interface=None, session: Session = None, **kwargs):
        super().__init__(**kwargs)
        self._interface = interface if interface else self.__interface_class__()
        self.session = session

    def set_attribute(self, name, value):
        setattr(self._interface, name, value)

    def get_attribute(self, name):
        return getattr(self._interface, name)

    def commit(self):
        self.session.commit()
