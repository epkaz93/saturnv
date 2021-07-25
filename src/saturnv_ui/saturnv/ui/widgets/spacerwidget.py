from Qt import QtWidgets
from Qt import QtCore
from Qt.QtCore import Qt


class SpacerWidget(QtWidgets.QWidget):

    def __init__(self, hSizePolicy=QtWidgets.QSizePolicy.Expanding, vSizePolicy=QtWidgets.QSizePolicy.Expanding,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(vSizePolicy, hSizePolicy)
