import re
from collections import deque
from pyschemaorg.loader import JSONSchemaLoader
try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO


class SchemaReader(object):
    def __init__(self, schema_file=None):
        self.loader = JSONSchemaLoader(schema_file)
        self._base_type = None
        self._types = None

    @property
    def base_type(self):
        '''
        Returns the name of the base type by finding the first type without
        any ancestors.

        '''
        if self._base_type is None:
            type_iter = self.loader.schema['types'].iteritems()
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
        types = self.loader.schema['types']
        while to_crawl:
            current = SchemaType(**types[to_crawl.popleft()])
            if current in visited:
                continue
            yield current
            visited.append(current)
            to_crawl.extend(current.subtypes)
        self._types = visited


class SchemaType(object):
    def __init__(self, id, ancestors=[], supertypes=[], properties=[],
                 specific_properties=[], instances=None, subtypes=[],
                 url=None, label=None, comment='', comment_plain=''):
        self.id = id
        self.properties = properties
        self.specific_properties = specific_properties
        self.supertypes = supertypes
        self.ancestors = ancestors
        self.instances = instances
        self.subtypes = subtypes
        self.url = url or 'http://schema.org/%s' % self.id
        self.label = label or re.sub("([a-z])([A-Z])","\g<1> \g<2>", id)
        self.comment = comment
        self.comment_plain = comment_plain

    def __repr__(self):  # pragma: no-cover
        return u''.join(('SchemaType(ancestors=%r, comment=%r, ',
                         'comment_plain=%r, id=%r, label=%r, properties=%r, ',
                         'specific_properties=%r, subtypes=%r, ',
                         'supertypes=%r, url=%r)')) % self
