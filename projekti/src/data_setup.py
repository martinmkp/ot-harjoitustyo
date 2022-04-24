import os
import numpy as np
import matplotlib.pyplot as plt


class SetUp:
    """
    Sets up text data for creating a word cloud.
    """

    def __init__(self, text):
        self.text = text
        self.text_modified = ""
        self.text_list = []
        self.word_counts = {}
        self.x_array = None
        self.y_array = None

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
        return self.word_counts

    def set_coordinates(self):
        """
        Sets random coordinates for the words.
        """
        self.x_array = np.random.uniform(
            low=-5, high=5, size=len(self.word_counts))
        self.y_array = np.random.uniform(
            low=-5, high=5, size=len(self.word_counts))
        return self.x_array, self.y_array
