from Qt import QtWidgets
from Qt.QtCore import Qt
from Qt import QtCore

from saturnv.ui import Application
from saturnv.ui.icons import icons


class Splash(QtWidgets.QMainWindow):

    startupComplete = QtCore.Signal()

    def __init__(self):
        super().__init__(windowTitle='SaturnV', flags=Qt.FramelessWindowHint, windowIcon=icons.application.saturnv)
        self.center()
        self._bottomToolBar = QtWidgets.QToolBar('BottomBar', movable=False, floatable=False)
        self.addToolBar(Qt.BottomToolBarArea, self.bottomToolBar())
        self._progressBar = QtWidgets.QProgressBar(textVisible=True)
        self.bottomToolBar().addWidget(self.progressBar())
        self.tasks = []

    def bottomToolBar(self):
        return self._bottomToolBar

    def progressBar(self):
        return self._progressBar

    def sizeHint(self):
        return QtCore.QSize(900, 500)

    def center(self):
        screen_geometry = Application.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)
