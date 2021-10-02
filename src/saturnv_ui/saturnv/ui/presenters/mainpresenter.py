from __future__ import annotations

from Qt import QtCore

import saturnv.api
import saturnv.api.repositories.base

from saturnv.ui.presenters import BasePresenter

import typing


class MainPresenter(BasePresenter):

    activePresetChanged = QtCore.Signal(saturnv.api.model.PresetModel)
    presetSelectionChanged = QtCore.Signal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._repository = saturnv.api.repository.Repository(saturnv.api.database.Session())
        self._preset_selection = []

    def repository(self) -> saturnv.api.repositories.base.AbstractRepository:
        return self._repository

    def activePreset(self) -> saturnv.api.model.PresetModel:
        return self.presetSelection()[0] if self.presetSelection() else None

    def presetSelection(self) -> typing.List[saturnv.api.model.PresetModel]:
        return self._preset_selection

    def setPresetSelection(self, presets):
        self._preset_selection = presets
        self.presetSelectionChanged.emit(presets)
        self.activePresetChanged.emit(self.activePreset())
