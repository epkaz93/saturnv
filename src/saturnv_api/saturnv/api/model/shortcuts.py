from datetime import datetime
from uuid import UUID

from saturnv.api.model.base import BaseModelItem, AbstractValueBase


class Shortcut(BaseModelItem):

    def __init__(self, version_uuid: UUID, author: str, creation_date: datetime = None, icon: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.version_uuid = version_uuid
        self.author = author
        self.creation_date = creation_date if datetime is not None else datetime.now()
        self.icon = icon


class Override(AbstractValueBase):

    def __init__(self, shortcut_uuid: UUID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shortcut_uuid = shortcut_uuid
