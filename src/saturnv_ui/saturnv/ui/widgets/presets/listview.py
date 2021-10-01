import functools

from Qt import QtWidgets, QtGui, QtCore


class PresetTreeView(QtWidgets.QTreeView):

    def __init__(self, model):
        super().__init__()
        proxy_model = QtCore.QSortFilterProxyModel()
        proxy_model.setSourceModel(model)
        self.setModel(proxy_model)
        self.model().setFilterKeyColumn(-1)

        self.header().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.header().customContextMenuRequested.connect(self.headerMenu)

        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        for index in range(self.model().columnCount()):
            self.resizeColumnToContents(index)

        self.setColumnHidden(1, True)
        self.setColumnHidden(4, True)

    def headerMenu(self, pos):
        menu = QtWidgets.QMenu()
        model = self.model().sourceModel()
        for index in range(self.model().columnCount()):
            action = QtWidgets.QAction(model.horizontalHeaderItem(index).text(), self, checkable=True, checked=not self.isColumnHidden(index))
            action.toggled.connect(functools.partial(self.setColumnHidden, index, not self.isColumnHidden(index)))
            menu.addAction(action)
        menu.exec(self.mapToGlobal(pos))
