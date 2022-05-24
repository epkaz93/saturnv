from __future__ import annotations

from pkg_resources import iter_entry_points
from functools import lru_cache

import typing

if typing.TYPE_CHECKING:
    from .baseplugin import PluginBase


class PluginManager(object):

    @lru_cache()
    def get_api_plugins(self) -> typing.List[PluginBase]:
        return [ep.load()() for ep in iter_entry_points('luna.api.plugins')]

    @lru_cache()
    def get_ui_plugins(self) -> typing.List[PluginBase]:
        return [ep.load()() for ep in iter_entry_points('luna.ui.plugins')]

    @lru_cache()
    def get_cli_plugins(self) -> typing.List[PluginBase]:
        return [ep.load()() for ep in iter_entry_points('luna.cli.plugins')]

    @lru_cache()
    def get_named_plugin(self, name) -> PluginBase:
        return next(iter([p for p in self.get_api_plugins() if p.name == name]))
