import pkg_resources
import json
try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO

SCHEMA_LOCATION = pkg_resources.resource_filename('pyschemaorg',
                                                  'schema/schema.json')


def get_schema(schema_location=SCHEMA_LOCATION):
    try:
        return open(schema_location)
    except IOError:
        return open(SCHEMA_LOCATION)


class SchemaLoader(object):  # pragma: no cover
    def __init__(self):
        self._schema = None

    @property
    def schema(self):
        raise NotImplementedError()


class JSONSchemaLoader(SchemaLoader):

    def __init__(self, schema_json=None):
        super(JSONSchemaLoader, self).__init__()
        self._schema_json = schema_json

    @property
    def schema(self):
        if self._schema is None:
            if self._schema_json is None:
                self._schema_json = get_schema()
            elif isinstance(self._schema_json, basestring):
                self._schema_json = get_schema(self._schema_json)
            self._schema = json.load(self._schema_json)
        return self._schema
