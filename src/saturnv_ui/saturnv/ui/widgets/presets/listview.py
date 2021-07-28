from Qt import QtWidgets


class PresetTreeView(QtWidgets.QTreeWidget):

    def __init__(self):
        super().__init__()
        self.setHeaderLabels([
            'uuid',
            'author',
            'versions',
            'description'
        ])

        self.setSortingEnabled(True)
