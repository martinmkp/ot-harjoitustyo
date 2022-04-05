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
    

    def test_koordinaatti_sanakirja_oikein(self):
        """
        Testaa, että koordinaattilistassa jokainen avain on str
        ja jokaisen arvon (tuple) molemmat elementit ovat float-muodossa.
        """
        key_counter = 0
        value_counter = 0
        for key in self.cloud.coordinate_dict:
            if type(key) != str:
                key_counter += 1
            if (
                self.cloud.coordinate_dict[key][0] != float 
                or 
                self.cloud.coordinate_dict[key][1] != float
                ):
                value_counter += 1

        self.assertEqual(key_counter, 0)
        self.assertEqual(value_counter, 0)
