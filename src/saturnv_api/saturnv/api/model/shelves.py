from pathlib import Path

from src.model.base import BaseModelItem


class Shelf(BaseModelItem):

    def __init__(self, name: str, path: str, author: str, *args, **kwargs):
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


class ShelfLink(BaseModelItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)