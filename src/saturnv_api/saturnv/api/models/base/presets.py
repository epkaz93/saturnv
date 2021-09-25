import six
import abc
import enum


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

    @property
    @abc.abstractmethod
    def versions(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def latest_version(self):
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

    @property
    @abc.abstractmethod
    def preset(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def settings(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def shortcuts(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractSettingModel(AbstractBaseValueModel):

    class Types(enum.Enum):
        package = 'package'
        envvar = 'envvar'
        command = 'command'
        # patch = 'patch'

    def __init__(self, **kwargs):
        if 'type' in kwargs and issubclass(kwargs['type'], self.Types):
            kwargs['type'] = kwargs['type'].value

        super().__init__(**kwargs)

    @property
    def version_uuid(self):
        return self.get_attribute('version_uuid')

    @property
    def type(self):
        return self.Types[super().type()]

    @property
    @abc.abstractmethod
    def version(self):
        raise NotImplementedError

    @classmethod
    def create_package_setting(cls, version_model: AbstractVersionModel, package: str, version: str = None):
        version_parts = str(version).split('.')
        value = {'version': version_parts}
        return cls(version_uuid=version_model.uuid, type=cls.Types.package.value, name=package, value=value)

    @classmethod
    def create_envvar_setting(cls, version_model: AbstractVersionModel, name: str, value: str = None, append=False):
        value = {'name': name, 'value': value, 'method': 'append' if append else 'set'}
        return cls(version_uuid=version_model.uuid, type=cls.Types.envvar.value, name=name, value=value)

    @classmethod
    def create_command_setting(cls, version_model: AbstractVersionModel, alias: str,  command: str):
        value = {'alias': alias, 'command': command}
        return cls(version_uuid=version_model.uuid, type=cls.Types.command.value, name=alias, value=value)


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

    @property
    @abc.abstractmethod
    def version(self):
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractOverrideModel(AbstractBaseValueModel):

    @property
    def shortcut_uuid(self):
        return self.get_attribute('shortcut_uuid')

    @property
    @abc.abstractmethod
    def shortcut(self):
        raise NotImplementedError
