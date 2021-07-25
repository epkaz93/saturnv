from Qt import QtCore
from Qt import QtWidgets

import code
import logging

from saturnv.ui.qtlogger import QtLoggers, get_logger

logger = get_logger('Console')
logger.setLevel(logging.DEBUG)


class ReadOnlyConsoleWidget(QtWidgets.QWidget):

    def __init__(self, showToolbar=False):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        for logger in QtLoggers.instance().loggers():
            self.addLogger(logger)

        QtLoggers.instance().loggerAdded.connect(self.addLogger)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self._output = QtWidgets.QPlainTextEdit(readOnly=True)
        self._toolbar = QtWidgets.QToolBar(visible=showToolbar)
        self.layout().addWidget(self._output)
        self.layout().addWidget(self.toolbar())

    def addLogger(self, logger):
        logger.messageWritten.connect(self.write)

    def toolbar(self):
        return self._toolbar

    @QtCore.Slot(str)
    def write(self, msg):
        self._output.appendPlainText(msg)

    def flush(self):
        pass


class InteractiveConsole(code.InteractiveConsole):

    def __init__(self, output, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._output = output

    def write(self, data):
        self._output.write(data)

    def runcode(self, code):
        self.write(f'>>> {code}')
        super().runcode(code)


class InteractiveConsoleWidget(ReadOnlyConsoleWidget):

    def __init__(self, showToolbar=True):
        super().__init__(showToolbar=showToolbar)

        context = dict(globals())
        context['print_'] = print
        context['print'] = self._print_function
        logger.warning('Overriding console print function. Use `print_` for original print')
        self._console = InteractiveConsole(self, context)
        self._input = QtWidgets.QLineEdit()
        self.toolbar().addWidget(self._input)
        self._input.returnPressed.connect(self._on_return_pressed)

    def _print_function(self, value):
        print(value)
        self.write(value)

    def _on_return_pressed(self):
        text = self._input.text()
        self.command(text)

    def console(self):
        return self._console

    @QtCore.Slot(str)
    def command(self, cmd):
        self.console().runcode(cmd)
