from pathlib import Path

from saturnv.model.base import BaseModelItem


class Shelve(BaseModelItem):

    def __init__(self, name: str, path: Path, author: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.path = path
        self.author = author

    def presets(self):
        pass

    def add_preset(self, preset):
        pass

    def remove_preset(self, preset):
        pass
