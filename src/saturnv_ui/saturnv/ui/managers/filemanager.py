from glob import glob
from pathlib import Path

from saturnv.ui.managers import AbstractBaseManager


class FileBasedManager(AbstractBaseManager):

    def __init__(self, path: Path, extension: str = '*'):
        super().__init__()
        self.path = path
        self.extension = extension

    @property
    def name(self):
        return self.path.stem

    def register_item(self, name: str, filepath: Path):
        super().register_item(name, filepath)

    def discover(self):
        for filename in glob(str(self.path / self.extension)):
            filepath = Path(filename)
            name = filepath.stem
            self.register_item(name, filepath)


class RecursiveFileBasedManager(FileBasedManager):

    def discover(self):
        super().discover()

        for dir_ in filter(lambda d: d.is_dir(), self.path.iterdir()):
            submanager = self.__class__(dir_)
            submanager.discover()
            self.register_sub_manager(submanager)
