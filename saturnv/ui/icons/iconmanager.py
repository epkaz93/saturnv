from glob import glob
from pathlib import Path


from Qt.QtGui import QIcon


class IconManager (object):

    def __init__(self, path: Path):
        self.path = path

    @property
    def name(self):
        return self.path.name

    def discover(self):
        for filename in glob(str(self.path / '*.png')):
            filepath = Path(filename)
            name = filepath.stem
            self.__setattr__(name, QIcon(str(filepath)))

        for dir_ in self.path.iterdir():
            if not dir_.is_dir():
                continue

            subengine = IconManager(dir_)
            subengine.discover()
            self.__setattr__(subengine.name, subengine)
