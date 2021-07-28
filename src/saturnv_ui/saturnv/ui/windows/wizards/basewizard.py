from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt

from src.ui import icons
from src.ui import SpacerWidget
from src.ui import PresenterWidgetMixin


class BaseWizardPresenter(QtCore.QObject):

    dataChanged = QtCore.Signal()


class BaseWizardPagePresenter(QtCore.QObject):

    dataChanged = QtCore.Signal()
    accepted = QtCore.Signal(bool)

    def __init__(self):
        super().__init__()
        self.dataChanged.connect(self.onDataChanged)

    def onDataChanged(self):
        self.accepted.emit(self.isAccepted())

    def isAccepted(self):
        raise NotImplementedError


class WizardPage(QtWidgets.QWidget, PresenterWidgetMixin):

    def __init__(self, name, icon, presenter, *args, **kwargs):

        PresenterWidgetMixin.__init__(self, presenter)
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self._name = name
        self._icon = icon


    def name(self):
        return self._name

    def icon(self):
        return self._icon


class Wizard(QtWidgets.QMainWindow, PresenterWidgetMixin):

    def __init__(self, presenter=None, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        PresenterWidgetMixin.__init__(self, presenter)

        self.resize(900, 750)
        self.setWindowIcon(icons.actions.add_preset)
        self._toolbar = QtWidgets.QToolBar('ActionBar', floatable=False, movable=False)
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar())
        self.toolbar().addWidget(QtWidgets.QLabel(pixmap=icons.actions.add_preset.pixmap(self.sizeHint() * 2.5)))
        self.toolbar().addWidget(SpacerWidget())

        self.btn_back = QtWidgets.QPushButton('&Back', enabled=False)
        self.btn_next = QtWidgets.QPushButton('&Next', enabled=False)
        self.btn_done = QtWidgets.QPushButton('&Done', enabled=False)

        self.toolbar().addWidget(self.btn_back)
        self.toolbar().addWidget(self.btn_next)
        self.toolbar().addWidget(self.btn_done)

        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setLayout(QtWidgets.QHBoxLayout())
        self._pageSelector = QtWidgets.QListWidget()
        self.pageSelector().setMaximumWidth(250)
        self._stackedWidget = QtWidgets.QStackedWidget()
        self.centralWidget().layout().addWidget(self.pageSelector())
        self.centralWidget().layout().addWidget(self.stackedWidget())

    def toolbar(self):
        return self._toolbar

    def pageSelector(self):
        return self._pageSelector

    def stackedWidget(self):
        return self._stackedWidget

    def add_page(self, page):
        self.pageSelector().addItem(QtWidgets.QListWidgetItem(page.icon(), page.name()))
        self.stackedWidget().addWidget(page)
        if self.pageSelector().count() == 1:
            self.pageSelector().setCurrentRow(0)