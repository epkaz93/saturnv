from Qt import QtWidgets


class ReadOnlyConsole(QtWidgets.QPlainTextEdit):

    def __init__(self):
        super().__init__(readOnly=True)
