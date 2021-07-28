from Qt import QtWidgets


class PresetModel(QtWidgets.QStandardItemModel):

    def __init__(self, repository):
        super().__init__(self)
        self._repository = repository

    def repository(self):
        return self._repository

