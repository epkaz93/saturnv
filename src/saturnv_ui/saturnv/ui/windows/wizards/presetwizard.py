from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from src.ui import icons

from . import Wizard, WizardPage, BaseWizardPagePresenter


class IconGridWidget(QtWidgets.QListWidget):
    def __init__(self, items):
        super().__init__()

        self.setMovement(QtWidgets.QListView.Static)
        self.setResizeMode(QtWidgets.QListView.Adjust)
        self.setGridSize(QtCore.QSize(64, 64))
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.selectionModel().selectionChanged.connect(self._selectionChanged)

        for item in items:
            self.addItem(item)

    def _selectionChanged(self, selected, deselected):
        if not selected:
            self.selectionModel().select(deselected, QtCore.QItemSelectionModel.Select)


class IconManagerGridWidget(IconGridWidget):

    def __init__(self, manager):

        def _get_icons(manager):
            icons = []
            for name, sub_manager in manager.iter_managers():
                icons.extend(_get_icons(sub_manager))

            for name, icon in manager.iter_icons():
                icons.append(QtWidgets.QListWidgetItem(icon, name))

            return icons

        super().__init__(_get_icons(manager))


class BasicPresetPagePresenter(BaseWizardPagePresenter):

    def __init__(self, name='', icon=None):
        super().__init__()

        self.name = ''
        self.icon = None

    def setName(self, name):
        self.name = name
        self.dataChanged.emit()

    def setIcon(self, icon):
        self.icon = icon
        self.dataChanged.emit()

    def isAccepted(self):
        return self.name and self.icon


class BasicPresetPage(WizardPage):

    def __init__(self, presenter):
        super().__init__(name='Basic Information', icon=icons.types.preset, presenter=presenter)

        self.setLayout(QtWidgets.QGridLayout())

        self.label_preset_name = QtWidgets.QLabel('Preset Name:')
        self.edit_preset_name = QtWidgets.QLineEdit(placeholderText='enter preset name')
        self.layout().addWidget(self.label_preset_name, 0, 0)
        self.layout().addWidget(self.edit_preset_name, 0, 1)

        self.label_preset_icon = QtWidgets.QLabel('Preset Icon:')
        self.layout().addWidget(self.label_preset_icon, 1, 0, Qt.AlignTop)

        self.view_preset_icon = IconManagerGridWidget(icons)
        self.layout().addWidget(self.view_preset_icon)

        self.view_preset_icon.setCurrentRow(0)


class NewPresetWizard(Wizard):
    def __init__(self, presenter, *args, **kwargs):
        super().__init__(presenter, *args, **kwargs)
        self.setWindowIcon(icons.actions.add_preset)
        self.add_page(BasicPresetPage(BasicPresetPagePresenter()))
