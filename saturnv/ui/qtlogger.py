import logging

from Qt import QtCore


class QtLoggers(QtCore.QObject):

    _instance = None
    _loggers = {}

    loggerAdded = QtCore.Signal(logging.Logger)

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def add_logger(self, name, logger):
        if name not in self._loggers:
            self._loggers[name] = logger
            self.loggerAdded.emit(logger)

    def loggers(self):
        for logger in self._loggers.values():
            yield logger


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
        self._defaultHandler.messageWritten.connect(self.messageWritten.emit)

    def defaultHandler(self):
        return self._defaultHandler


logging.setLoggerClass(QtLogger)


def get_logger(name):
    logger = logging.getLogger(name)
    QtLoggers.instance().add_logger(name, logger)

    return logger
