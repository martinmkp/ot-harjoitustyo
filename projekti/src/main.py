import numpy as np
import os
from wordcloud import WordCloud

if __name__ == "__main__":
    # a relative path starting from the main folder of the project 
    # (/projekti/)
    dir = "data_folder/tekstidata.txt"
    wordcloud = WordCloud()
    wordcloud.read_txt(dir)
    wordcloud.modify_text()
    wordcloud.count_words()
    wordcloud.set_coordinates()
