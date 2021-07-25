from datetime import datetime

from saturnv.api.model.base import BaseModelItem


class Preset(BaseModelItem):

    def __init__(self, author, creation_date: datetime = None, deleted=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.author = author
        self.creation_date = creation_date if creation_date is not None else datetime.now()
        self.deleted = deleted
        self._current_version_uuid = None
        self._versions = []

    def fetch_versions(self):
        self._versions = self._repository.versions_from_preset(self)
        if self._versions:
            self._current_version_uuid = self.versions[0].uuid
        return self._versions

    @property
    def versions(self):
        return self._versions

    def shortcuts(self):
        pass

    def shelves(self):
        pass

    @property
    def current_version(self):
        for version in self.versions:
            if version.uuid == self._current_version_uuid:
                return version
            
    @property
    def latest(self):
        return self.current_version

    @property
    def name(self):
        return self.current_version.name