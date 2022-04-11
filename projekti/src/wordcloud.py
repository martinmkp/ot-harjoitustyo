import os
import numpy as np
import matplotlib.pyplot as plt


class WordCloud:

    def __init__(self):
        self.text = ""
        self.text_modified = ""
        self.text_list = []
        self.punctuation = [".", ",", "?", "!", "/"]
        self.special_punctuation = ["/"]
        self.coordinate_dict = {}
        self.word_counts = {}
        self.x_array = None
        self.y_array = None

    def read_txt(self, dir, encode="utf-8"):
        """
        Reads a txt-file
        """
        fullpath = os.path.join(os.getcwd()[:-9], dir)
        print("Path:\n", fullpath)
        try:
            with open(fullpath, encoding=encode) as file:
                self.text = ''.join(file.readlines())
            print("Text data read successfully.")

        except Exception as e:
            print("An exception occurred:\n", e)

    def modify_text(self):
        """
        Modifies the text data (string) by:
        - setting all characters lower case
        - removing punctuation marks 
        """
        self.text_modified = self.text.lower()
        for i in self.punctuation:
            if i in self.special_punctuation:
                self.text_modified = self.text_modified.replace(i, " ")
            else:
                self.text_modified = self.text_modified.replace(i, "")
        print("Punctuation marks removed")

    def string_to_list(self):
        self.text_list = list(self.text.split(" "))
        print("A list of words created from the string.")

    def count_words(self):
        """
        Counts the occurrences of each unique word in the list
        """
        self.word_counts = {word: 0 for word in set(self.text_list)}
        for word in self.text_list:
            self.word_counts[word] += 1
        self.word_counts = sorted(
            self.word_counts.items(), key=lambda x: x[1], reverse=True)

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
