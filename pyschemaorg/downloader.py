from contextlib import closing
import urllib2


URL = 'http://schema.rdfs.org/all.json'


def get_schema_json():
    return urllib2.urlopen(URL).read()


if __name__ == '__main__':
    f = open('schema.json', 'w')
    f.write(get_schema_json())
    f.close()

