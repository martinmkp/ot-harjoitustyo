from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import unittest
from reader import Reader
from data_setup import SetUp


class TestDataSetUp(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()
        self.dir = "projekti/data_folder/tekstidata.txt"
        self.text_data = self.reader.read_txt(self.dir)
        self.setup = SetUp(self.text_data, "s")

    def test_punctuation_mark_removal_works(self):
        punctuation = [".", ",", "?", "!", "/"]
        counter = 0
        self.setup.modify_text()

        for char in self.setup.text_modified:
            if char in punctuation:
                counter += 1
        self.assertEqual(counter, 0)

    def test_word_dict_includes_all_words(self):
        counter = 0
        self.setup.modify_text()
        self.setup.string_to_list()
        words_dict = self.setup.count_words()
        for element in words_dict:
            counter += element[1]
        self.assertEqual(counter, len(self.setup.text_list))
