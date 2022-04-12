from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER
import unittest
from wordcloud import WordCloud


class TestWordCloud(unittest.TestCase):
    def setUp(self):
        self.cloud = WordCloud()

    def test_valimerkit_poistettu(self):
        marker_counter = 0
        # Note: more markers will be added to this list
        # as the project progresses
        marker_list = [".", ",", "?", "!", "/"]
        for char in self.cloud.text_modified:
            if char in marker_list:
                marker_counter += 1

        self.assertEqual(marker_counter, 0)

    def test_suuret_kirjaimet_poistettu(self):
        uppercase_counter = 0
        uppercase_list = 0
        for char in self.cloud.text_modified:
            if char.isupper():
                uppercase_counter += 1

        self.assertEqual(uppercase_counter, 0)

    def test_koordinaatit_keskiarvo(self):
        """
        Testaa että koordinaatit ovat järkevästi jakautuneet,
        eli keskiarvo lähellä nollaa.
        """
        dir = "projekti/data_folder/tekstidata.txt"
        self.cloud.read_txt(dir)
        self.cloud.modify_text()
        self.cloud.string_to_list()
        self.cloud.count_words()
        self.cloud.set_coordinates()
        x_sum = 0.0
        y_sum = 0.0
        x_avg = 0.0
        y_avg = 0.0
        for num in self.cloud.x_array:
            x_sum += num
        for num in self.cloud.y_array:
            y_sum += num
        x_avg = x_sum/len(self.cloud.x_array)
        y_avg = y_sum/len(self.cloud.y_array)

        self.assertGreaterEqual(x_avg , -2.5)
        self.assertGreaterEqual(y_avg , -2.5)
        self.assertLessEqual(x_avg , 2.5)
        self.assertLessEqual(y_avg , 2.5)