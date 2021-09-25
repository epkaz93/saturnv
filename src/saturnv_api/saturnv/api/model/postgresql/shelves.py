from saturnv.api import database
from saturnv.api.model import base


from .basemodel import PostgresqlBaseModelMixin


class ShelfModel(PostgresqlBaseModelMixin, base.AbstractShelfModel):

    __interface_class__ = database.Shelf

    def __init__(self, interface=None, **kwargs):
        PostgresqlBaseModelMixin.__init__(self, interface)
        super().__init__(**kwargs)
