from Qt import QtWidgets, QtCore, QtGui

from saturnv.ui.presenters import PresenterWidgetMixin, MainPresenter
from saturnv.ui.images import screenshots
from saturnv.ui.widgets import SpacerWidget


class PresetEditorView(QtWidgets.QWidget, PresenterWidgetMixin):

    def __init__(self, presenter: MainPresenter):
        super().__init__(presenter=presenter)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self._headerImage = QtWidgets.QLabel()
        self._presetTitle = QtWidgets.QLabel()
        self._presetTitle.setStyleSheet('font-size: 16pt;')
        font = QtGui.QFont()
        font.setBold(True)
        self._presetTitle.setFont(font)
        self._presetDescription = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setItalic(True)
        self._presetDescription.setFont(font)

        self.headerImage().setScaledContents(True)
        self.headerImage().setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        self.headerImage().setFixedHeight(400)

        self.layout().addWidget(self.headerImage(), QtCore.Qt.AlignCenter)
        self.layout().addWidget(self._presetTitle)
        self.layout().addWidget(self._presetDescription)
        self.layout().addWidget(SpacerWidget())

        self.refreshUI()

        self.presenter().activePresetChanged.connect(self.refreshUI)

    def refreshUI(self):
        preset = self.preset()
        if not preset:
            return
        latest_version = self.preset().latest_version

        header_image = preset.metadata.get('header_image') or latest_version.metadata.get('header_image')
        header_image = screenshots.screenshot_from_string(header_image) if header_image else QtGui.QPixmap('')
        self.setHeaderImage(header_image)
        self.setPresetTitle(latest_version.name)
        self.setPresetDescription(latest_version.description)

    def headerImage(self):
        return self._headerImage

    def setHeaderImage(self, image):
        self.headerImage().setPixmap(image)

    def setPresetTitle(self, text):
        return self._presetTitle.setText(text)

    def setPresetDescription(self, text):
        return self._presetDescription.setText(text)

    def presenter(self) -> MainPresenter:
        return super().presenter()

    def preset(self):
        return self.presenter().activePreset()

    def closeEvent(self, event):
        self.presenter().presetChanged.disconnect(self.refreshUI)
        super().closeEvent(event)
