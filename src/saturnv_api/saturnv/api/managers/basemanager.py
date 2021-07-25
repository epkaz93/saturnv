from abc import ABC


class BaseManager(ABC):

    def discover(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()
