import os
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

if __name__ == "__main__":
    dir = "projekti/data_folder/tekstidata.txt"
    wordcloud = WordCloud()
    wordcloud.read_txt(dir)
    wordcloud.modify_text()
    wordcloud.string_to_list()
    wordcloud.count_words()
    wordcloud.set_coordinates()
    wordcloud.plot_words()
