from Qt.QtWidgets import QApplication
from Qt.QtCore import Qt


class Application(QApplication):

    pass


Application.setAttribute(Qt.AA_EnableHighDpiScaling)
