from saturnv.ui.managers import FileBasedManager


class FontManager(FileBasedManager):

    def __init__(self, path, extension='*ttf'):
        super().__init__(path, extension)
