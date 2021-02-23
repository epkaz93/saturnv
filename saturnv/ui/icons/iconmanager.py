from glob import glob
from pathlib import Path

from saturnv.manager import FileBasedManager

from Qt.QtGui import QIcon


class IconManager (FileBasedManager):

    def __init__(self, path: Path):
        self.path = path

    def discover(self):
        for filename in glob(str(self.path / '*.png')):
            filepath = Path(filename)
            name = filepath.stem
            self.__setattr__(name, QIcon(str(filepath)))

        for dir_ in self.path.iterdir():
            if not dir_.is_dir():
                continue

            submanager = self.__class__(dir_)
            submanager.discover()
            self.__setattr__(submanager.name, submanager)
