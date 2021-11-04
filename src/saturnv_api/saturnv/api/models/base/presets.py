from __future__ import annotations

import six
import abc
import enum
from datetime import datetime, timedelta

from . import AbstractBaseModel, AbstractBaseValueModel

import typing


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

    @deleted.setter
    def deleted(self, value):
        self.set_attribute('deleted', value)

    @property
    @abc.abstractmethod
    def versions(self) -> typing.List[AbstractVersionModel]:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def latest_version(self) -> AbstractVersionModel:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def version_count(self) -> int:
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class AbstractVersionModel(AbstractBaseModel):

    @property
    def name(self):
        return self.get_attribute('name')

    @name.setter
    def name(self, value):
        self.set_attribute('name', value)

    @property
    def icon(self):
        return self.get_attribute('icon')

    @icon.setter
    def icon(self, value):
        self.set_attribute('icon', value)

    @property
    def description(self):
        return self.get_attribute('description')

    @description.setter
    def description(self, value):
        self.set_attribute('description', value)

    @property
    def preset_uuid(self):
        return self.get_attribute('creation_date')

    @property
    def creation_date(self) -> datetime:
        return self.get_attribute('creation_date')

    @property
    def fuzzy_creation_date(self):
        now = datetime.now()
        if self.creation_date.date() == now.date():
            return self.creation_date.strftime('%I:%M %p')
        if self.creation_date > now - timedelta(days=7):
            return self.creation_date.strftime('%A %I:%M %p')

        return self.creation_date.strftime('%d %b %Y %I:%M %p')

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

    @property
    def packages(self):
        return [s for s in self.settings if isinstance(s, AbstractPackageSettingModel)]

    @property
    def environment_variables(self):
        return [s for s in self.settings if isinstance(s, AbstractEnvironmentVariableSettingModel)]

    @property
    def commands(self):
        return [s for s in self.settings if isinstance(s, AbstractCommandSettingModel)]


@six.add_metaclass(abc.ABCMeta)
class AbstractSettingModel(AbstractBaseValueModel):

    class Types(enum.Enum):
        package = 'package'
        envvar = 'envvar'
        command = 'command'
        # patch = 'patch'

    def __init__(self, **kwargs):
        if 'type' in kwargs and isinstance(kwargs['type'], enum.Enum):
            kwargs['type'] = kwargs['type'].value

        super(AbstractSettingModel, self).__init__(**kwargs)

    @property
    def version_uuid(self):
        return self.get_attribute('version_uuid')

    @property
    def type(self):
        super_type = super(AbstractSettingModel, self).type
        return self.Types(super_type) if super_type in [t.value for t in self.Types] else super_type

    @property
    @abc.abstractmethod
    def version(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<{self.__class__.__name__}> {self.name} {self.value}'


@six.add_metaclass(abc.ABCMeta)
class AbstractPackageSettingModel(AbstractSettingModel):

    class Comparisons(enum.Enum):
        equals = '=='
        weak = '~'
        not_equals = '!='
        greater_than = '>'
        less_then = '<'
        greater_than_equals = '>='
        less_then_equals = '<='

    def __init__(self, package: str, version: str = None, comparison: Comparisons = Comparisons.equals, **kwargs):
        version_parts = str(version).split('.') if version else []
        comparison = comparison.value if isinstance(comparison, enum.Enum) else comparison
        value = {'version': version_parts, 'comparison': comparison}
        super(AbstractPackageSettingModel, self).__init__(name=package, value=value, type=self.Types.package.value, **kwargs)

    @property
    def package(self):
        return self.name

    @property
    def version_(self):
        return self.value.get('version', [])

    @property
    def comparison(self):
        return self.Comparisons(self.value.get('comparison', self.Comparisons.equals.value))

    @property
    def version_str(self):
        return '.'.join([str(x) for x in self.value.get('version')])

    def get_version_part(self, i):
        return self.version_[i] if i < len(self.version_) else None

    @property
    def major(self):
        return self.get_version_part(0)

    @property
    def minor(self):
        return self.get_version_part(1)

    @property
    def patch(self):
        return self.get_version_part(2)

    @property
    def point(self):
        return self.get_version_part(3)

    def __str__(self):
        return f'{self.package}{self.comparison.value}{self.version_str}' if self.version_ else self.package

    def __repr__(self):
        return f'<{self.__class__.__name__} "{self}">'


@six.add_metaclass(abc.ABCMeta)
class AbstractEnvironmentVariableSettingModel(AbstractSettingModel):

    class Methods(enum.Enum):
        append = 'append'
        set = 'set'
        substitute = 'substitute'

    def __init__(self, name, value, method=Methods.set, **kwargs):
        value = {'value': value, 'method': method.value}
        super(AbstractEnvironmentVariableSettingModel, self).__init__(name=name, value=value, type=self.Types.envvar, **kwargs)

    @property
    def variable_value(self):
        return self.value['value']

    @property
    def variable_name(self):
        return self.name

    @property
    def variable_method(self):
        return self.Methods(self.value.get('method', self.Methods.set.value))


@six.add_metaclass(abc.ABCMeta)
class AbstractCommandSettingModel(AbstractSettingModel):

    def __init__(self, alias, command, **kwargs):
        value = {'alias': alias, 'command': command}
        super(AbstractCommandSettingModel, self).__init__(name=alias, value=value, type=self.Types.command, **kwargs)

    @property
    def alias(self):
        return self.value['alias']

    @property
    def command(self):
        return self.value['command']


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
