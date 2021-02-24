from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from saturnv.ui.icons import icons
from saturnv.ui.widgets import SpacerWidget


class MainWindowMenuToolBar(QtWidgets.QToolBar):

    def __init__(self):
        super().__init__('MenuBar', movable=False, floatable=False)

        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setIconSize(QtCore.QSize(20, 20))

        self._menuBar = QtWidgets.QMenuBar()
        self.menuBar().setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.addWidget(self.menuBar())

        self.spacer = SpacerWidget()
        self.spacer_action = self.addWidget(self.spacer)

        self.separator_action = self.addSeparator()
        self._searchBar = QtWidgets.QLineEdit(placeholderText='search')
        self.addWidget(self.searchBar())

    def menuBar(self):
        return self._menuBar

    def searchBar(self):
        return self._searchBar

    def packEnd(self, widget):
        if isinstance(widget, QtWidgets.QAction):
            self.insertAction(self.separator_action, widget)
        else:
            self.insertWidget(self.separator_action, widget)

    def packStart(self, widget):
        if isinstance(widget, QtWidgets.QAction):
            self.insertAction(self.spacer_action, widget)
        else:
            self.insertWidget(self.spacer_action, widget)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__(windowTitle='SaturnV Launcher', windowIcon=icons.application.saturnv)

        self._menuToolBar = MainWindowMenuToolBar()
        self.addToolBar(self.menuToolBar())

        self.refresh_action = QtWidgets.QAction(icons.actions.refresh, '&Refresh', self)
        self.menuToolBar().packEnd(self.refresh_action)

        self.addToolBarBreak(Qt.TopToolBarArea)

        self._applicationToolBar = self.addToolBar('ApplicationToolBar')
        self.applicationToolBar().setIconSize(QtCore.QSize(20, 20))
        self.applicationToolBar().setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.action_new_preset = QtWidgets.QAction(icons.actions.add, '&New Preset', self)
        self.applicationToolBar().addAction(self.action_new_preset)
        self.action_delete_preset = QtWidgets.QAction(icons.actions.delete, '&Delete Preset', self)
        self.applicationToolBar().addAction(self.action_delete_preset)
        self.action_edit_preset = QtWidgets.QAction('&Edit Preset', self)
        self.action_new_shelf = QtWidgets.QAction(icons.actions.add_folder, '&New Shelf', self)
        self.applicationToolBar().addAction(self.action_new_shelf)
        self.action_browse_shelves = QtWidgets.QAction('&Browse', self)

        self.file_menu = self.menuBar().addMenu('&File')
        self.preset_menu = self.menuBar().addMenu('&Preset')
        self.shelf_menu = self.menuBar().addMenu('&Shelf')
        self.help_menu = self.menuBar().addMenu('&Help')

        self.preset_menu.addAction(self.action_new_preset)
        self.preset_menu.addAction(self.action_delete_preset)

        self.shelf_menu.addAction(self.action_new_shelf)
        self.shelf_menu.addAction(self.action_browse_shelves)


    def menuToolBar(self) -> MainWindowMenuToolBar:
        return self._menuToolBar

    def applicationToolBar(self):
        return self._applicationToolBar

    def menuBar(self):
        return self.menuToolBar().menuBar()

    def sizeHint(self):
        return QtCore.QSize(900, 500)
