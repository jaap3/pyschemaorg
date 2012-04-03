from collections import deque
import json


class SchemaWalker(object):

    def __init__(self, schema_location):
        self.schema_location = schema_location

    @property
    def schema_location(self):
        return self._schema_location

    @schema_location.setter
    def schema_location(self, schema_location):
        self._schema_location = schema_location
        self._schema = None
        self._base_type = None

    @property
    def schema(self):
        if self._schema is None:
            f = open(self.schema_location)
            self._schema = json.load(f)
        return self._schema

    @property
    def base_type(self):
        if self._base_type is None:
            type_iter = self.schema['types'].iteritems()
            while not self._base_type:
                type_name, properties = type_iter.next()
                if not properties['ancestors']:
                    self._base_type = type_name
        return self._base_type

    def type_walker(self):
        visited = set()
        to_crawl = deque([self.base_type])
        while to_crawl:
            current = to_crawl.popleft()
            if current in visited:
                continue
            yield current
            visited.add(current)
            to_crawl.extend(self.schema['types'][current]['subtypes'])
