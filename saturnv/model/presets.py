from datetime import datetime

from saturnv.model.base import BaseModelItem


class Preset(BaseModelItem):

    def __init__(self, author: str, creation_date: datetime = None, deleted=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.author = author
        self.creation_date = creation_date if creation_date is not None else datetime.now()
        self.deleted = deleted

    def versions(self):
        pass

    def shortcuts(self):
        pass

    def shelves(self):
        pass
