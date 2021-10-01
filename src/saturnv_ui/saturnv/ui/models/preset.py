from __future__ import annotations

import enum

from Qt import QtWidgets, QtCore, QtGui

from saturnv.ui.icons import icons

import typing

if typing.TYPE_CHECKING:
    from saturnv.api.models.base import AbstractPresetModel


class PresetItemModel(QtGui.QStandardItemModel):

    def __init__(self, presets: typing.List[AbstractPresetModel]):
        super().__init__()
        self.setPresets(presets)
        header_labels = [
            'Name',
            'UUID',
            'Author',
            'Modified',
            'Versions',
            'Description'
        ]
        self.setHorizontalHeaderLabels(header_labels)
        self.setColumnCount(len(header_labels))

    def setPresets(self, presets):
        self._presets = presets
        self.setRowCount(len(presets))

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        preset = self.presets()[index.row()]

        if index.column() == 0:
            if preset.latest_version.name != value:
                preset.latest_version.name = value
                preset.latest_version.commit()
                return True

        if index.column() == 5:
            if preset.latest_version.description != value:
                preset.latest_version.description = value
                preset.latest_version.commit()
                return True

        return False

    def flags(self, index):
        if index.column() in [0, 5]:
            return super().flags(index)
        return super().flags(index) ^ QtCore.Qt.ItemIsEditable

    def data(self, index, role=QtCore.Qt.DisplayRole):
        preset = self.presets()[index.row()]
        latest_version = preset.latest_version
        if index.column() == 0:
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                return latest_version.name
            if role == QtCore.Qt.DecorationRole:
                icon = icons.icon_from_string(latest_version.icon) if latest_version.icon else icons.types.preset
                return icon
        if index.column() == 1:
            if role == QtCore.Qt.DisplayRole:
                return str(preset.uuid)
        if index.column() == 2:
            if role == QtCore.Qt.DisplayRole:
                return preset.author
        if index.column() == 3:
            if role == QtCore.Qt.DisplayRole:
                return f'{latest_version.fuzzy_creation_date} ({latest_version.blame})'
        if index.column() == 4:
            if role == QtCore.Qt.DisplayRole:
                return preset.version_count
        if index.column() == 5:
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                return latest_version.description

        return super().data(index, role)

    def presets(self):
        return self._presets
