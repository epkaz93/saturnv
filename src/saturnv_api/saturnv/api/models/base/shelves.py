import six
import abc


from . import AbstractBaseModel


@six.add_metaclass(abc.ABCMeta)
class AbstractShelfModel(AbstractBaseModel):

    @property
    def name(self):
        return self.get_attribute('name')

    @property
    def author(self):
        return self.get_attribute('author')

    @property
    def path(self):
        return self.get_attribute('path')

    @property
    @abc.abstractmethod
    def presets(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def versions(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def shortcuts(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_preset(self, preset):
        raise NotImplementedError

    @abc.abstractmethod
    def add_version(self, preset):
        raise NotImplementedError

    @abc.abstractmethod
    def add_shortcut(self, preset):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_preset(self, preset):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_version(self, preset):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_shortcut(self, preset):
        raise NotImplementedError
