import enum
from datetime import datetime
from uuid import UUID

from src.model.base import BaseModelItem, AbstractValueBase

import typing
from typing import Dict, Union, List


class Version(BaseModelItem):

    def __init__(self, name, preset_uuid: UUID, blame: str, creation_date: datetime = None, icon: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name
        self.preset_uuid = preset_uuid
        self.blame = blame
        self.creation_date = creation_date
        self.icon = icon


class Setting(AbstractValueBase):

    class Types(enum.Enum):
        package = 'package'

    def __init__(self, version_uuid: UUID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.version_uuid = version_uuid

    @classmethod
    def create_package_setting(cls, version_uuid: UUID, package: str, version: str = None):
        version_parts = str(version).split('.')
        value = version_parts if version_parts else []
        version = {'version': value}
        return Setting(version_uuid=version_uuid, type=Setting.Types.package.value, name=package, value=version)
