from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from saturnv.ui.icons import icons


class MainWindowMenuToolBar(QtWidgets.QToolBar):

    def __init__(self):
        super().__init__('MenuBar', movable=False, floatable=False)

        self.setContextMenuPolicy(Qt.NoContextMenu)

        self._menuBar = QtWidgets.QMenuBar()
        self.menuBar().setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addWidget(self.menuBar())
        self.file_menu = self.menuBar().addMenu('&File')
        self.help_menu = self.menuBar().addMenu('&Help')

        self.spacer = QtWidgets.QWidget()
        self.spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.addWidget(self.spacer)
        self._searchBar = QtWidgets.QLineEdit(placeholderText='search')
        self.addWidget(self.searchBar())

    def menuBar(self):
        return self._menuBar

    def searchBar(self):
        return self._searchBar


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__(windowTitle='SaturnV Launcher', windowIcon=icons.application.saturnv)

        self._menuToolBar = MainWindowMenuToolBar()
        self.addToolBar(self.menuToolBar())

    def menuToolBar(self):
        return self._menuToolBar

    def menuBar(self):
        return self.menuToolBar().menuBar()

    def sizeHint(self):
        return QtCore.QSize(900, 500)
