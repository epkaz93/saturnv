from abc import ABC
from pathlib import Path


class BaseManager (object):

    def discover(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()


class FileBasedManager(BaseManager, ABC):

    def __name__(self, path: Path):
        super().__init__()
        self.path = path

    @property
    def name(self):
        return self.path.stem
