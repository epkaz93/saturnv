import six
import abc

from saturnv.api.models.base import AbstractPresetModel, AbstractShelfModel

import typing


@six.add_metaclass(abc.ABCMeta)
class AbstractRepository(object):

    def __init__(self, session):
        self._session = session

    @abc.abstractmethod
    def get_presets(self, deleted=False) -> typing.List[AbstractPresetModel]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_shelves(self, deleted=False) -> typing.List[AbstractShelfModel]:
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self):
        return self._session.commit()
