import json
from pyschemaorg import downloader
try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO


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
                self._schema_json = StringIO(downloader.get_schema_json())
            self._schema = json.load(self._schema_json)
        return self._schema
