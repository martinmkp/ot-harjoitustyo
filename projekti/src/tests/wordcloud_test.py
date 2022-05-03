from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import unittest
from xml.dom import WrongDocumentErr
import matplotlib
from data_setup import SetUp
from reader import Reader
from database import DataBase
from wordcloud import WordCloud


class TestWordCloud(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()
        self.directory = "projekti/data_folder/tekstidata.txt"
        self.text_data = self.reader.read_txt(self.directory)
        self.setup = SetUp(self.text_data)
        self.setup.modify_text()
        self.setup.string_to_list()
        self.words_count = self.setup.count_words()
        self.x_coordinates, self.y_coordinates = self.setup.set_coordinates()
        self.wordcloud = WordCloud(
            self.words_count, self.x_coordinates, self.y_coordinates)

    def test_coordinates_are_consistent(self):
        len_x_array = len(self.wordcloud.x_array)
        len_y_array = len(self.wordcloud.y_array)
        self.assertEqual(len_x_array, len_y_array)

    def test_plot_annotated_correctly(self):
        self.wordcloud.plot_words("sanapilvi")
        len_x_array = len(self.wordcloud.x_array)
        annotations = [child for child in self.wordcloud.axes.get_children(
        ) if isinstance(child, matplotlib.text.Annotation)]
        self.assertEqual(len(annotations), len_x_array)
