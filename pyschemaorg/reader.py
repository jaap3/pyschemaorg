from collections import deque
from pyschemaorg.loader import JSONSchemaLoader
try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO


class SchemaReader(object):

    def __init__(self, schema_loader=None):
        if schema_loader is None:
            schema_loader = JSONSchemaLoader()
        self._loader = schema_loader
        self._base_type = None
        self._types = None

    @property
    def base_type(self):
        '''
        Returns the name of the base type by finding the first type without
        any ancestors.

        '''
        if self._base_type is None:
            type_iter = self._loader.schema['types'].iteritems()
            while not self._base_type:
                type_name, properties = type_iter.next()
                if not properties['ancestors']:
                    self._base_type = type_name
        return self._base_type

    @property
    def types(self):
        if not self._types:
            return self._type_walker()
        return self._types

    def _type_walker(self):
        visited = list()
        to_crawl = deque([self.base_type])
        types = self._loader.schema['types']
        while to_crawl:
            current = to_crawl.popleft()
            if current in visited:
                continue
            yield current
            visited.append(current)
            to_crawl.extend(types[current]['subtypes'])
        self._types = visited
