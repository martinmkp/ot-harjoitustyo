import os
import numpy as np
import matplotlib.pyplot as plt


class WordCloud:
    """
    This class contains the functionalities to create
    a word cloud. It: 
    - takes a .txt file as an input & reads it to a str variable
    - removes punctuation marks and sets upper case char to lower case
    - splits the string to a list of words
    - draws a 2d wordcloud from the list of words
    - saves the plot to the root of this project as sanapilvi.png
    """

    def __init__(self):
        self.text = ""
        self.text_modified = ""
        self.text_list = []
        self.word_counts = {}
        self.x_array = None
        self.y_array = None

    def read_txt(self, dir, encode="utf-8"):
        """
        Reads a txt-file
        """
        fullpath = os.path.join(os.getcwd()[:-9], dir)
        print("Reading the data file from the path:\n", fullpath)
        try:
            with open(fullpath, encoding=encode) as file:
                self.text = ''.join(file.readlines())
            print("\nText data read successfully.")

        except Exception as e:
            print("An exception occurred:\n", e)

    def modify_text(self):
        """
        Modifies the text data (string) by:
        - setting all characters lower case
        - removing punctuation marks 
        """
        print("\nRemoving the punctuation marks...")
        punctuation = [".", ",", "?", "!", "/"]
        special_punctuation = "/"
        self.text_modified = self.text.lower()
        for i in punctuation:
            if i == special_punctuation:
                self.text_modified = self.text_modified.replace(i, " ")
            else:
                self.text_modified = self.text_modified.replace(i, "")
        print("Punctuation marks removed.")

    def string_to_list(self):
        "Transforms the string to a list of words."
        print("\nCreating a list of words...")
        self.text_list = list(self.text_modified.split(" "))
        print("A list of words created from the string.")

    def count_words(self):
        """
        Counts the occurrences of each unique word in the list
        """
        print("\nCounting the frequencies of the words...")
        self.word_counts = {word: 0 for word in set(self.text_list)}
        for word in self.text_list:
            self.word_counts[word] += 1
        self.word_counts = sorted(
            self.word_counts.items(), key=lambda x: x[1], reverse=True)
        print("Frequencies calculated. The most frequent word is:\n",
              self.word_counts[0][0], "with", self.word_counts[0][1], "appearances.")

    def set_coordinates(self):
        """
        Sets random coordinates for the words.
        """
        self.x_array = np.random.uniform(
            low=-5, high=5, size=len(self.word_counts))
        self.y_array = np.random.uniform(
            low=-5, high=5, size=len(self.word_counts))

    def plot_words(self):
        """
        Creates a wordcloud. The size of the words is defined
        by number of their appearnce in the given dataset.
        """
        print("\nCreating a wordcloud...")
        # Set up colors
        colors = ["#069AF3", "#13EAC9", "#90EE90", "#00FF00"]
        curr_color = ""

        # Set up the plot
        fig, ax = plt.subplots()
        ax.scatter(self.x_array, self.y_array, color='white', marker=',')

        # Add the words to the invisible markers in the plot as annotations
        for i, label in enumerate(list(self.word_counts)):
            if i < len(self.word_counts) // 4:
                curr_color = colors[0]
            elif i < len(self.word_counts) // 2:
                curr_color = colors[1]
            elif i < 3 * len(self.word_counts) // 4:
                curr_color = colors[2]
            else:
                curr_color = colors[3]
            ax.annotate(label[0], (self.x_array[i], self.y_array[i]),
                        size=8+label[1]*3, color=curr_color)

        # Removes the axis
        ax.axis("off")
        # Saves the figure
        fig.savefig("sanapilvi.png")
        print("Wordcloud created and saved successfully.")
