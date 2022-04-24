import os
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from data_setup import SetUp
from reader import Reader

if __name__ == "__main__":
    dir = "projekti/data_folder/tekstidata.txt"

    reader = Reader()
    text_data = reader.read_txt(dir)

    setup = SetUp(text_data)
    setup.modify_text()
    setup.string_to_list()
    words_count = setup.count_words()
    x_coordinates, y_coordinates = setup.set_coordinates()

    wordcloud = WordCloud(words_count, x_coordinates, y_coordinates)
    wordcloud.plot_words()


