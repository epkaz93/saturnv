import six
import abc
from uuid import uuid4


@six.add_metaclass(abc.ABCMeta)
class AbstractBaseModel(object):

    def __init__(self, **kwargs):
        for key, value in filter(lambda i: i[1] is not None, kwargs.items()):
            self.set_attribute(key, value)

    @property
    def uuid(self):
        return self.get_attribute('uuid')

    @uuid.setter
    def uuid(self, uuid):
        self.set_attribute('uuid', uuid)

    @property
    def metadata(self):
        return self.get_attribute('metadata')

    @uuid.setter
    def uuid(self, metadata):
        self.set_attribute('metadata', metadata)

    @abc.abstractmethod
    def get_attribute(self, name):
        raise NotImplementedError

    @abc.abstractmethod
    def set_attribute(self, name, value):
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractBaseValueModel(AbstractBaseModel):

    @property
    def type(self):
        return self.get_attribute('type')

    @property
    def name(self):
        return self.get_attribute('name')

    @property
    def icon(self):
        return self.get_attribute('icon')

    @property
    def value(self):
        return self.get_attribute('value')

