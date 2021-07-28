from Qt import QtWidgets


class VersionTreeView(QtWidgets.QTreeWidget):

    def __init__(self):
        super().__init__()
        self.setHeaderLabels([
            'name',
            'blame',
            'icon',
            'creation_date'
        ])

        self.setSortingEnabled(True)