import abc


class PluginBase(object, metaclass=abc.ABCMeta):

    def __init__(self):
        self._loaded = False
        self.to_load = False

    @property
    @abc.abstractmethod
    def name(self):
        """"""

    @property
    @abc.abstractmethod
    def long_name(self):
        """"""

    @property
    @abc.abstractmethod
    def description(self):
        """"""

    @property
    @abc.abstractmethod
    def version(self):
        """"""

    @property
    @abc.abstractmethod
    def type(self):
        """"""

    @property
    @abc.abstractmethod
    def author(self):
        """"""

    @property
    def loaded(self):
        return self._loaded

    @classmethod
    @abc.abstractmethod
    def _load(cls):
        """"""

    def load(self):
        self._load()
        self._loaded = True

    @property
    def to_load(self):
        return self._to_load

    @to_load.setter
    def to_load(self, state):
        self._to_load = state
