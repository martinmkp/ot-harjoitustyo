from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import unittest
from database import DataBase


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase()

    def test_db_returns_lists(self):
        self.db.connect_db()
        x, y, word_count = self.db.read_from_db("testaus")
        self.assertEqual(type(x), list)
        self.assertEqual(type(y), list)
        self.assertEqual(type(word_count), list)

    def test_elements_of_lists_from_db_have_correct_type(self):
        self.db.connect_db()
        x, y, word_count = self.db.read_from_db("testaus")
        self.assertEqual(type(x[0]), float)
        self.assertEqual(type(y[0]), float)
        self.assertEqual(type(word_count[0]), tuple)
