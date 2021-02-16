import sys

from saturnv.ui import Application
from Qt.QtCore import QTimer


def load_application(splash):

    count = 0
    max_ = 40

    def increment():
        nonlocal count
        count += 1
        splash.progressBar().setValue(count)

    splash.progressBar().setMaximum(max_)

    timer = QTimer(interval=50, singleShot=False)
    timer.timeout.connect(increment)
    timer.start()
    return timer


if __name__ == '__main__':
    app = Application(sys.argv)

    from saturnv.ui.windows import Splash

    splash = Splash()
    splash.show()

    state = load_application(splash)

    sys.exit(app.exec_())
