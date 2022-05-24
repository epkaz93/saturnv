from __future__ import annotations

import unittest

from pathlib import Path

from luna.plugin.pluginmanager import PluginManager

import typing
if typing.TYPE_CHECKING:
    from yaml_datasource.api.repository import YAMLRepository

REPO_PATH = Path(__file__).parent / 'resources'
plugin_manager = PluginManager()


class TestPresets(unittest.TestCase):

    def setUp(self) -> None:
        plugin = plugin_manager.get_named_plugin('yaml_api_plugin')
        plugin.load()
        import luna.api.repository

        self.repo: YAMLRepository = luna.api.repository.yaml.YAMLRepository(REPO_PATH)
        self.presets = list(self.repo.get_all_presets())

    def test_instantiation(self):
        presets = self.presets
        presets = [p for p in presets]

        files = [f for f in (REPO_PATH / 'presets').glob('*.yaml')]
        self.assertEqual(len(presets), len(files))
        self.assertIn('blender', [p.name for p in presets])
