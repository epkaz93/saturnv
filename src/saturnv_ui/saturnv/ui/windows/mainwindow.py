from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from saturnv.ui.icons import icons
from saturnv.ui.widgets import SpacerWidget
from saturnv.ui.widgets.presets import PresetTreeView
from saturnv.ui.models.preset import PresetItemModel
from saturnv.ui.widgets.presets import PresetEditorView

from saturnv.ui.presenters import PresenterWidgetMixin, MainPresenter


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
        QtWidgets.QMainWindow.__init__(self, windowTitle='SaturnV Launcher')
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

        self.setCentralWidget(QtWidgets.QSplitter(orientation=QtCore.Qt.Horizontal))
        self.preset_view = PresetTreeView(model=PresetItemModel(presets=self.presenter().repository().get_presets()))
        self.preset_view.presetSelectionChanged.connect(self.presenter().setPresetSelection)
        self.preset_settings = PresetEditorView(self.presenter())
        self.centralWidget().addWidget(self.preset_view)
        self.centralWidget().addWidget(self.preset_settings)
        #self.centralWidget().setStretchFactor(0, 5)
        #self.centralWidget().setStretchFactor(1, 2)

        self.menuToolBar().searchBar().textChanged.connect(self.preset_view.model().setFilterRegExp)
        self.refresh_action.triggered.connect(self.refresh_presets)

    def refresh_presets(self):
        self.preset_view.model().sourceModel().setPresets(self.presenter().repository().get_presets())

    def menuToolBar(self) -> MainWindowMenuToolBar:
        return self._menuToolBar

    def applicationToolBar(self):
        return self._applicationToolBar

    def menuBar(self):
        return self.menuToolBar().menuBar()

    def sizeHint(self):
        return QtCore.QSize(900, 500)
