from abc import ABC
from pathlib import Path

from saturnv.managers import BaseManager


class FileBasedManager(BaseManager, ABC):

    def __init__(self, path: Path):
        super().__init__()
        self.path = path

    @property
    def name(self):
        return self.path.stem
