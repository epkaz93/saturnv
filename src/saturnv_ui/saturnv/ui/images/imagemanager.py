import functools

from saturnv.ui.managers import RecursiveFileBasedManager

from Qt import QtGui


class ScreenshotManager(RecursiveFileBasedManager):

    def __init__(self, path, extension='*.png'):
        super().__init__(path, extension)

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if name in self._items.keys():
            return self.get_image(attr)
        else:
            return attr

    @functools.lru_cache()
    def get_image(self, image) -> QtGui.QImage:
        return QtGui.QImage(image)
