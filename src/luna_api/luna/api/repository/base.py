from __future__ import annotations

import abc
import uuid

import typing
if typing.TYPE_CHECKING:
    from ..model.preset import Preset
    from ..query.base import QueryBase


class RepositoryBase(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_all_presets(self) -> typing.Iterable[Preset]:
        """"""

    @abc.abstractmethod
    def get_preset_by_id(self, id_: uuid.UUID) -> Preset:
        """"""

    @abc.abstractmethod
    def query(self, operators) -> QueryBase:
        """"""


class NullRepository(RepositoryBase):

    def get_all_presets(self) -> None:
        return None

    def get_preset_by_id(self, id_: uuid.UUID) -> None:
        return None

    def query(self, operators):
        return None