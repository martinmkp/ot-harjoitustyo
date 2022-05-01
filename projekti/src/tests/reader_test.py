from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import unittest
from reader import Reader


class TestReader(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()

    def test_reader_works(self):
        directory = "projekti/data_folder/tekstidata.txt"
        text_data = self.reader.read_txt(directory)
        data_type = type(text_data)
        self.assertEqual(data_type, str)
