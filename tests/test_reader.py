import os.path
import unittest2
from pyschemaorg.reader import SchemaReader


SCHEMA_LOCATION = os.path.join(os.path.dirname(__file__),
                               'data', 'schema.json')


class SchemaReaderTest(unittest2.TestCase):
    def setUp(self):
        self.reader = SchemaReader(open(SCHEMA_LOCATION))

    def test_get_base(self):
        self.assertEquals('Thing', self.reader.base_type)

    def test_get_types(self):
        self.assertEquals(set(self.reader.types),
                          set(self.reader.loader.schema['types'].keys()))


@unittest2.skip('Disabled so it will not hammer schema.rdfs.org.')
class TestReaderWithDownload(SchemaReaderTest):
    def setUp(self):
        super(TestReaderWithDownload, self).setUp()
        self.reader = SchemaReader()
