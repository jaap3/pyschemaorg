import os.path
import unittest
from pyschemaorg.walker import SchemaWalker

SCHEMA_LOCATION = os.path.join(os.path.dirname(__file__),
                               'data', 'schema.json')


class TestWalker(unittest.TestCase):

    def setUp(self):
        self.stw = SchemaWalker(SCHEMA_LOCATION)

    def test_get_base(self):
        self.assertEquals('Thing', self.stw.base_type)

    def test_get_types(self):
        self.assertEquals(set(self.stw.type_walker()),
                          set(self.stw.schema['types'].keys()))