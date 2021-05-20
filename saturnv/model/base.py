from uuid import UUID, uuid4

from typing import Dict


class BaseModelItem(object):

    def __init__(self, uuid: UUID = None, metadata: Dict = None):
        self.uuid = uuid if uuid is not None else uuid4()
        self.metadata = metadata if metadata is not None else {}


class AbstractValueBase(BaseModelItem):

    def __init__(self, name: str, type: str, value: Dict, icon: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name
        self.type = type
        self.value = value
        self.icon = icon