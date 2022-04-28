from __future__ import annotations

import io
import uuid

import yaml

from .base import RepositoryBase
from ..model.preset import Preset
from ..query.yaml import YAMLQuery

import typing
if typing.TYPE_CHECKING:
    from pathlib import Path


class YAMLRepository(RepositoryBase):

    def get_preset_by_id(self, id_: uuid.UUID) -> Preset:
        pass

    def query(self, type_) -> YAMLQuery:
        return YAMLQuery(type_, repository=self)

    def __init__(self, path: Path):
        super().__init__()
        self.path = path

    def get_all_presets(self) -> typing.Iterator[Preset]:
        for file in (self.path / 'presets').glob('*.yaml'):
            with io.open(file) as f:
                data = yaml.safe_load(f.read())
            preset = Preset.from_dict(data)
            yield preset
