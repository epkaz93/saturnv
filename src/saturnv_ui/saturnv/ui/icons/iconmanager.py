from __future__ import annotations

from Qt.QtGui import QIcon

from saturnv.ui.managers import RecursiveFileBasedManager

import typing
if typing.TYPE_CHECKING:
    from pathlib import Path


class IconManager(RecursiveFileBasedManager):

    def __init__(self, path, extension='*.png'):
        super().__init__(path, extension=extension)

        self._managers = []
        self._icons = []

    def icon_from_string(self, path: str) -> QIcon:
        parts = path.split('.')
        if len(parts) == 1:
            return getattr(self, parts[0])
        else:
            return getattr(self, parts[0]).icon_from_string('.'.join(parts[1:]))

    def register_item(self, name: str, filepath: Path) -> QIcon:
        icon = QIcon(str(filepath))
        super().register_item(name, icon)
