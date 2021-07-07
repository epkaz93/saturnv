from glob import glob
from pathlib import Path

from saturnv.managers import FileBasedManager

from Qt.QtGui import QIcon


class IconManager(FileBasedManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._managers = []
        self._icons = []

    def icon_from_string(self, path):
        parts = path.split('.')
        if len(parts) == 1:
            return self.__getattribute__(parts[0])
        else:
            return self.__getattribute__(parts[0]).icon_from_string('.'.join(parts[1:]))

    def discover(self):
        for filename in glob(str(self.path / '*.png')):
            filepath = Path(filename)
            name = filepath.stem
            self.__setattr__(name, QIcon(str(filepath)))
            self._icons.append((name, self.__getattribute__(name)))

        for dir_ in self.path.iterdir():
            if not dir_.is_dir():
                continue

            submanager = self.__class__(dir_)
            submanager.discover()
            self.__setattr__(submanager.name, submanager)
            self._managers.append((submanager.name, submanager))

    def __iter__(self):
        yield from self.iter_managers()
        yield from self.iter_icons()

    def iter_managers(self):
        for name, manager in self._managers:
            yield name, manager

    def iter_icons(self):
        for name, icon in self._icons:
            yield name, icon
