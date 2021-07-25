from glob import glob
from pathlib import Path
import sass

from Qt import QtWidgets

from src.managers import FileBasedManager


class ThemeManager(FileBasedManager):

    _current_theme = None

    def discover(self):
        for filename in glob(str(self.path / '*.scss')):
            filepath = Path(filename)
            name = filepath.stem
            self.__setattr__(name, Theme(name, filepath))

    @property
    def current_theme(self):
        return self._current_theme

    @current_theme.setter
    def current_theme(self, theme):
        self._current_theme = theme
        if QtWidgets.QApplication.instance():
            QtWidgets.QApplication.instance().setStyleSheet(theme.data)

    @property
    def has_default(self):
        return hasattr(self, 'default')


class Theme(object):

    def __init__(self, name, filepath):

        self.name = name
        self.filepath = filepath
        self._data = self.load_data()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        self._filepath = filepath

    def load_data(self):
        return sass.compile(filename=str(self.filepath))

    @property
    def data(self):
        return self._data
