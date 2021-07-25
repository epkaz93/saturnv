import sys
import logging

from Qt.QtCore import QTimer
from Qt import QtGui

from src.ui import Application
from src.ui import get_logger


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

    from src.ui import Splash

    from src.ui.themes import themes
    from src.ui import fonts

    if themes.has_default:
        themes.current_theme = themes.default

    QtGui.QFontDatabase.addApplicationFont(str(fonts.roboto_slab))
    logger.info('Loading Splash')

    splash = Splash()
    logger.info('Logger Connected')
    logger.info('Starting Imports')

    from src.ui import MainWindow
    from src.ui import MainPresenter

    win = MainWindow(MainPresenter())
    #win = wizards.NewPresetWizard(wizards.BaseWizardPresenter())
    splash.startupComplete.connect(win.show)
    splash.startupComplete.connect(splash.close)
    splash.show()

    logger.info('Connecting to API')
    logger.info('Loading Shelves')
    logger.info('Loading Presets')

    state = load_application(splash)

    sys.exit(app.exec_())
