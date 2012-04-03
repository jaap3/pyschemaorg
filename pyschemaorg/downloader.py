import urllib2


URL = 'http://schema.rdfs.org/all.json'


def get_schema_json(output_file):
    response = urllib2.urlopen(URL)
    with open(output_file, 'w') as f:
        for line in response:
            f.write(line)


if __name__ == '__main__':
    get_schema_json('schema.json')
