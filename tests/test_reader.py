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
        self.assertEquals(
            set([schema_type.id for schema_type in self.reader.types]),
            set(self.reader.loader.schema['types'].keys()))

    def test_types_are_returned_in_correct_order(self):
        '''
        Tests that all types are returned in base -> subtype order.

        Simply iterating over all types and checking if its ancestors
        have already been processed does the trick.
        '''
        returned = []
        for schema_type in self.reader.types:
            returned.append(schema_type.id)
            if schema_type:
                for ancestor in schema_type.ancestors:
                    self.assertIn(ancestor, returned)


@unittest2.skip('Disabled so it will not hammer schema.rdfs.org.')
class TestReaderWithDownload(SchemaReaderTest):
    def setUp(self):
        super(TestReaderWithDownload, self).setUp()
        self.reader = SchemaReader()
