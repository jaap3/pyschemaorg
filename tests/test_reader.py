import os.path
import unittest2
from pyschemaorg.loader import JSONSchemaLoader
from pyschemaorg.reader import SchemaReader


SCHEMA_LOCATION = os.path.join(os.path.dirname(__file__),
                               'data', 'schema.json')


class BaseWalkerTest(unittest2.TestCase):
    def setUp(self):
        self.loader = JSONSchemaLoader(open(SCHEMA_LOCATION))
        self.schema_reader = SchemaReader(self.loader)

    def test_get_base(self):
        self.assertEquals('Thing', self.schema_reader.base_type)

    def test_get_types(self):
        self.assertEquals(set(self.schema_reader.types),
                          set(self.loader.schema['types'].keys()))


@unittest2.skip('Disabled so it will not hammer schema.rdfs.org.')
class TestWalkerWithDownload(BaseWalkerTest):
    def setUp(self):
        self.loader = JSONSchemaLoader()
        super(TestWalkerWithDownload, self).setUp()
