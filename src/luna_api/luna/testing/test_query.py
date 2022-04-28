import unittest
from parameterized import parameterized

from pathlib import Path

from luna.api.model.preset import Preset
from luna.api.query.base import QueryBase
from luna.api.query import operators

from luna.api.repository.base import NullRepository
from luna.api.repository.yaml import YAMLRepository

REPO_PATH = Path(__file__).parent / 'resources'


class TestQuery(unittest.TestCase):

    def test_equals(self):
        query = QueryBase(Preset.name == 'test', repository=NullRepository())
        self.assertEqual(len(query.operators), 1)
        self.assertIs(Preset.name, query.operators[0].field)
        self.assertIsInstance(query.operators[0], operators.EqualsOperator)

    def test_greaterthan_equals(self):
        query = QueryBase(Preset.name >= 'test', repository=NullRepository())
        self.assertEqual(len(query.operators), 1)
        self.assertIs(Preset.name, query.operators[0].field)
        self.assertIsInstance(query.operators[0], operators.GreaterThanEqualsOperator)

    def test_multiple_operators(self):
        query = QueryBase(Preset.name == 'blender', Preset.name >= 'test', repository=NullRepository())
        self.assertEqual(len(query.operators), 2)
        self.assertIs(Preset.name, query.operators[0].field)
        self.assertIs(Preset.name, query.operators[1].field)
        self.assertIsInstance(query.operators[0], operators.EqualsOperator)
        self.assertIsInstance(query.operators[1], operators.GreaterThanEqualsOperator)

    def test_logical_and(self):
        query = QueryBase((Preset.name == 'blender') & (Preset.name >= 'test'), repository=NullRepository())
        self.assertEqual(len(query.operators), 1)
        self.assertIsInstance(query.operators[0], operators.AndOperator)
        self.assertIsInstance(query.operators[0].a, operators.EqualsOperator)
        self.assertIsInstance(query.operators[0].b, operators.GreaterThanEqualsOperator)

    def test_logical_or(self):
        query = QueryBase((Preset.name != 'blender') | (Preset.name < 'test'), repository=NullRepository())
        self.assertEqual(len(query.operators), 1)
        self.assertIsInstance(query.operators[0], operators.OrOperator)
        self.assertIsInstance(query.operators[0].a, operators.NotEqualsOperator)
        self.assertIsInstance(query.operators[0].b, operators.LessThanOperator)

    def test_explicit_and(self):
        query = QueryBase(operators.AndOperator(Preset.name == 'blender', Preset.name == 'test'), repository=NullRepository())
        self.assertEqual(len(query.operators), 1)
        self.assertIsInstance(query.operators[0], operators.AndOperator)
        self.assertIsInstance(query.operators[0].a, operators.EqualsOperator)
        self.assertIsInstance(query.operators[0].b, operators.EqualsOperator)

    def test_create_operator(self):
        operator = operators.OperatorMeta.create_operator('==', Preset.name, 'test')
        self.assertIs(Preset.name, operator.field)
        self.assertIsInstance(operator, operators.EqualsOperator)


class TestQueryOperation(unittest.TestCase):

    def setUp(self) -> None:
        self.repo = YAMLRepository(REPO_PATH)
        self.cached_presets = list(self.repo.get_all_presets())

    @parameterized.expand([
        ((Preset.name == 'blender',), 1),
        ((Preset.name == 'blender', Preset.name != 'blender'), 0),
        (((Preset.name == 'blender') | (Preset.name == "luna"),), 2),
        ((Preset.name != '',), 2)
    ])
    def test_query_yaml(self, operators, expected_length):
        query = self.repo.query(*operators)
        presents = list(query.fetch())
        self.assertEqual(expected_length, len(presents))
        """
        query = self.repo.query(Preset.name == 'blender', Preset.name != "blender")
        presents = list(query.fetch())
        self.assertEqual(0, len(presents))

        query = self.repo.query((Preset.name == 'blender') | (Preset.name == "luna"))
        presents = list(query.fetch())
        self.assertEqual(2, len(presents))

        query = self.repo.query(Preset.name != '')
        presents = list(query.fetch())
        self.assertEqual(2, len(presents))

        query = self.repo.query(((Preset.name == 'blender') | (Preset.name == "luna")) & (Preset.name != ''))
        presents = list(query.fetch())
        self.assertEqual(2, len(presents))
        """