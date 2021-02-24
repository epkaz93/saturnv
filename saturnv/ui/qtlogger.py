import logging

from Qt import QtCore


class QtLogHandler(logging.StreamHandler, QtCore.QObject):

    messageWritten = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        super(QtCore.QObject, self).__init__()
        self.setFormatter(logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s'))

    def emit(self, record):
        super().emit(record)
        self.messageWritten.emit(self.format(record))


class QtLogger(logging.Logger, QtCore.QObject):

    messageWritten = QtCore.Signal(str)

    def __init__(self, name):
        super().__init__(name)
        super(QtCore.QObject, self).__init__()
        self._defaultHandler = QtLogHandler()
        self.addHandler(self._defaultHandler)

    def defaultHandler(self):
        return self._defaultHandler


logging.setLoggerClass(QtLogger)


def get_logger(name):
    logger = logging.getLogger(name)

    return logger
