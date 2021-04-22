import sys
import logging

from Qt.QtCore import QTimer
from Qt import QtGui

from saturnv.ui import Application
from saturnv.ui.qtlogger import get_logger


logger = get_logger('Application')
logger.setLevel(logging.INFO)


def load_application(splash):

    count = 0
    max_ = 10

    def increment():
        nonlocal count, max_
        logger.info(f'Doing task {count}')
        count += 1
        splash.progressBar().setValue(count)
        if count == max_:
            splash.startupComplete.emit()
            timer.stop()

    splash.progressBar().setMaximum(max_)

    timer = QTimer(interval=50, singleShot=False)
    timer.timeout.connect(increment)
    timer.start()
    return timer


if __name__ == '__main__':
    app = Application(sys.argv)

    from saturnv.ui.windows import Splash

    from saturnv.ui.themes import themes
    from saturnv.ui.fonts import fonts

    if themes.has_default:
        themes.current_theme = themes.default

    QtGui.QFontDatabase.addApplicationFont(str(fonts.roboto_slab))
    logger.info('Loading Splash')

    splash = Splash()
    logger.info('Logger Connected')
    logger.info('Starting Imports')

    from saturnv.ui.windows import MainWindow
    win = MainWindow()
    splash.startupComplete.connect(win.show)
    splash.startupComplete.connect(splash.close)
    splash.show()

    from saturnv import api
    logger.info('Connecting to API')
    logger.info('Loading Shelves')
    logger.info('Loading Presets')

    state = load_application(splash)

    sys.exit(app.exec_())
