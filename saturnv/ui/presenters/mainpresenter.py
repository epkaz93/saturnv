from Qt import QtCore


class MainPresenter(QtCore.QObject):

    def __init__(self, configuration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._configuration = configuration
        self._repository = PresetRepository()

    @property
    def configuration(self):
        return self._configuration