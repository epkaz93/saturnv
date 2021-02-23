import sys

from Qt.QtCore import QTimer

from saturnv.ui import Application


def load_application(splash):

    count = 0
    max_ = 10

    def increment():
        nonlocal count, max_
        count += 1
        splash.progressBar().setValue(count)
        if count == max_:
            splash.startupComplete.emit()

    splash.progressBar().setMaximum(max_)

    timer = QTimer(interval=50, singleShot=False)
    timer.timeout.connect(increment)
    timer.start()
    return timer


if __name__ == '__main__':
    app = Application(sys.argv)

    from saturnv.ui.windows import Splash
    from saturnv.ui.windows import MainWindow

    splash = Splash()
    win = MainWindow()
    splash.startupComplete.connect(win.show)
    splash.startupComplete.connect(splash.close)
    splash.show()

    state = load_application(splash)

    sys.exit(app.exec_())
