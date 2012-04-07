import unittest
from pyschemaorg import writer
from pyschemaorg import reader


class TestWriter(unittest.TestCase):
    def setUp(self):
        self.reader = reader.SchemaReader()
        self.writer = writer.PythonWriter()

    def test_python_code_generator(self):
        pass

