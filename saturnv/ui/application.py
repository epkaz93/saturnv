from Qt.QtWidgets import QApplication
from Qt.QtCore import Qt


class Application(QApplication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setApplicationName('SaturnV Launcher')


Application.setAttribute(Qt.AA_EnableHighDpiScaling)
