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
