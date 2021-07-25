from glob import glob
from pathlib import Path

from src.managers import FileBasedManager


class FontManager(FileBasedManager):

    def discover(self):
        for filename in glob(str(self.path / '*.ttf')):
            filepath = Path(filename)
            name = filepath.stem
            self.__setattr__(name, filepath)
