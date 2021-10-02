import functools

from saturnv.ui.managers import RecursiveFileBasedManager

from Qt import QtGui


class ScreenshotManager(RecursiveFileBasedManager):

    def __init__(self, path, extension='*.png'):
        super().__init__(path, extension)

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        items = super().__getattribute__('_items')
        get_image = ScreenshotManager.get_image
        if name in items.keys():
            return get_image(self, attr)
        else:
            return attr

    @functools.lru_cache()
    def get_image(self, image) -> QtGui.QPixmap:
        return QtGui.QPixmap(str(image))

    def screenshot_from_string(self, path: str) -> QtGui.QPixmap:
        parts = path.split('.')
        if len(parts) == 1:
            return getattr(self, (parts[0]))
        else:
            return getattr(self, parts[0]).screenshot_from_string('.'.join(parts[1:]))
