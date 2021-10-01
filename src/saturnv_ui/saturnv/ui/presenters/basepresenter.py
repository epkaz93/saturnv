from Qt import QtCore


class BasePresenter(QtCore.QObject):
    pass


class PresenterWidgetMixin(QtCore.QObject):

    def __init__(self, presenter):
        super().__init__()
        self._presenter = presenter

    def presenter(self) -> BasePresenter:
        return self._presenter
