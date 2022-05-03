from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
from re import X
import unittest
import numpy as np
from ui_text import TextInterface


class TestTextInterface(unittest.TestCase):
    def setUp(self):
        self.text_inter = TextInterface("projekti/data_folder/")
        self.text_inter.wordcloud_filename = "sanapilvi"
        self.text_inter.db_question = "n"

    def test_data_array_types_with_datafile(self):
        self.text_inter.data_source_type = "t"
        self.text_inter.textdata_name = "tekstidata.txt"
        x_array, y_array, words_count = self.text_inter.execute_data_preprocessing()
        self.assertEqual(type(x_array), np.ndarray)
        self.assertEqual(type(y_array), np.ndarray)
        self.assertEqual(type(words_count), list)

    def test_data_array_types_with_database(self):
        self.text_inter.data_source_type = "s"
        self.text_inter.row_name = "testaus"
        x_array, y_array, words_count = self.text_inter.execute_data_preprocessing()
        self.assertEqual(type(x_array), list)
        self.assertEqual(type(y_array), list)
        self.assertEqual(type(words_count), list)
