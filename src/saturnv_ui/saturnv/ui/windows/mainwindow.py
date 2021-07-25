from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from src.ui import icons
from src.ui import SpacerWidget
from src.ui.widgets.presets import PresetTreeView

from src.ui import PresenterWidgetMixin, MainPresenter


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


class MainWindow(QtWidgets.QMainWindow, PresenterWidgetMixin):

    def __init__(self, presenter: MainPresenter):
        QtWidgets.QMainWindow.__init__(self, windowTitle='SaturnV Launcher', windowIcon=icons.application.saturnv)
        PresenterWidgetMixin.__init__(self, presenter)

        print(self.presenter().repository)

        self._menuToolBar = MainWindowMenuToolBar()
        self.addToolBar(self.menuToolBar())

        self.refresh_action = QtWidgets.QAction(icons.actions.refresh, '&Refresh', self)
        self.menuToolBar().packEnd(self.refresh_action)

        self.addToolBarBreak(Qt.TopToolBarArea)

        self._applicationToolBar = self.addToolBar('ApplicationToolBar')
        self.applicationToolBar().setIconSize(QtCore.QSize(20, 20))
        self.applicationToolBar().setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.action_new_preset = QtWidgets.QAction(icons.actions.add_preset, '&New Preset', self)
        self.applicationToolBar().addAction(self.action_new_preset)
        #self.action_new_preset.triggered.connect()
        self.action_delete_preset = QtWidgets.QAction(icons.actions.delete_preset, '&Delete Preset', self)
        self.applicationToolBar().addAction(self.action_delete_preset)
        self.action_edit_preset = QtWidgets.QAction('&Edit Preset', self)
        self.action_new_shelf = QtWidgets.QAction(icons.actions.add_shelf, '&New Shelf', self)
        self.applicationToolBar().addAction(self.action_new_shelf)
        self.action_delete_shelf = QtWidgets.QAction(icons.actions.delete_shelf, '&Delete Shelf', self)
        self.applicationToolBar().addAction(self.action_delete_shelf)
        self.action_browse_shelves = QtWidgets.QAction('&Browse', self)

        self.file_menu = self.menuBar().addMenu('&File')
        self.preset_menu = self.menuBar().addMenu('&Preset')
        self.shelf_menu = self.menuBar().addMenu('&Shelf')
        self.help_menu = self.menuBar().addMenu('&Help')

        self.preset_menu.addAction(self.action_new_preset)
        self.preset_menu.addAction(self.action_delete_preset)

        self.shelf_menu.addAction(self.action_new_shelf)
        self.shelf_menu.addAction(self.action_delete_shelf)
        self.shelf_menu.addAction(self.action_browse_shelves)

        self.setCentralWidget(PresetTreeView())
        for preset in self.presenter().repository().all_presets():
            item = QtWidgets.QTreeWidgetItem()

            item.setData(1, Qt.DisplayRole, preset.author)
            versions = self.presenter().repository().versions_from_preset(preset)
            print(versions)
            latest = versions[0] if versions else None
            icon = icons.icon_from_string(latest.icon) if latest and latest.icon else icons.types.preset
            if latest:
                item.setData(0, Qt.DisplayRole, latest.name)
                item.setData(2, Qt.DisplayRole, str(len(versions)))
                item.setData(3, Qt.DisplayRole, latest.description)
            else:
                item.setData(0, Qt.DisplayRole, str(preset.uuid))


            item.setData(0, Qt.DecorationRole, icon)
            self.centralWidget().addTopLevelItem(item)

    def menuToolBar(self) -> MainWindowMenuToolBar:
        return self._menuToolBar

    def applicationToolBar(self):
        return self._applicationToolBar

    def menuBar(self):
        return self.menuToolBar().menuBar()

    def sizeHint(self):
        return QtCore.QSize(900, 500)
