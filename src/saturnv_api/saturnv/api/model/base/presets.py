import six
import abc


from . import AbstractBaseModel, AbstractBaseValueModel


@six.add_metaclass(abc.ABCMeta)
class AbstractPresetModel(AbstractBaseModel):

    @property
    def creation_date(self):
        return self.get_attribute('creation_date')

    @property
    def author(self):
        return self.get_attribute('author')

    @property
    def deleted(self):
        return self.get_attribute('deleted')

    @abc.abstractmethod
    @property
    def versions(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractVersionModel(AbstractBaseModel):

    @property
    def name(self):
        return self.get_attribute('name')

    @property
    def icon(self):
        return self.get_attribute('icon')

    @property
    def description(self):
        return self.get_attribute('description')

    @property
    def preset_uuid(self):
        return self.get_attribute('creation_date')

    @property
    def creation_date(self):
        return self.get_attribute('creation_date')

    @property
    def blame(self):
        return self.get_attribute('blame')

    @abc.abstractmethod
    @property
    def preset(self):
        raise NotImplementedError

    @abc.abstractmethod
    @property
    def settings(self):
        raise NotImplementedError

    @abc.abstractmethod
    @property
    def shortcuts(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractSettingModel(AbstractBaseValueModel):

    @property
    def version_uuid(self):
        return self.get_attribute('version_uuid')

    @abc.abstractmethod
    @property
    def version(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractShortcutModel(AbstractBaseModel):

    @property
    def version_uuid(self):
        return self.get_attribute('version_uuid')

    @property
    def icon(self):
        return self.get_attribute('icon')

    @property
    def creation_date(self):
        return self.get_attribute('creation_date')

    @property
    def author(self):
        return self.get_attribute('author')

    @abc.abstractmethod
    @property
    def version(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractOverrideModel(AbstractBaseModel):

    @property
    def shortcut_uuid(self):
        return self.get_attribute('shortcut_uuid')

    @abc.abstractmethod
    @property
    def shortcut(self):
        raise NotImplementedError