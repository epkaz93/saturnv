import unittest

from pathlib import Path

from luna.api.model.preset import Preset

from luna.api.repository.yaml import YAMLRepository

REPO_PATH = Path(__file__).parent / 'resources'


class TestPresets(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = YAMLRepository(REPO_PATH)
        self.presets = list(self.repo.get_all_presets())

    def test_instantiation(self):
        presets = self.presets
        presets = [p for p in presets]

        files = [f for f in (REPO_PATH / 'presets').glob('*.yaml')]
        self.assertEqual(len(presets), len(files))
        self.assertIn('blender', [p.name for p in presets])
