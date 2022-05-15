import numpy as np


class SetUp:
    """A class for setting up data for a word cloud.

    Attributes:
        text: A text data input (assumed to be a string).
    """

    def __init__(self, text, shape):
        """Constructor.

        Args:
            text: Input text data (assumed to be a string).
        """
        self.__text = text
        self.__word_counts = {}
        self.__x_array = None
        self.__y_array = None
        self.__shape = shape
        self.text_modified = ""
        self.text_list = []

    def modify_text(self):
        """ Modifies the text data (string) by setting all characters lower case
        and removing punctuation marks """
        punctuation = [".", ",", "?", "!", "/",
                       ":", ";", "[", "]", "(", ")", "-", "&"]
        special_punctuation = "/"
        self.text_modified = self.__text.lower()
        for i in punctuation:
            if i == special_punctuation:
                self.text_modified = self.text_modified.replace(i, " ")
            else:
                self.text_modified = self.text_modified.replace(i, "")

    def string_to_list(self):
        """Transforms the string to a list of words."""
        self.text_list = list(self.text_modified.split(" "))

    def count_words(self):
        """Counts the occurrences of each unique word in the list
        """
        self.__word_counts = {word: 0 for word in set(self.text_list)}
        for word in self.text_list:
            self.__word_counts[word] += 1
        self.__word_counts = sorted(
            self.__word_counts.items(), key=lambda x: x[1], reverse=True)
        return self.__word_counts

    def set_coordinates(self):
        """Sets random coordinates for the words.
        """
        n_words = len(self.__word_counts)
        radius = 5
        theta = 2 * np.pi * np.random.rand(n_words, 1)
        r_squared = radius * np.sqrt(np.random.rand(n_words, 1))

        if self.__shape == "s":
            self.__x_array = np.random.uniform(
                low=-5, high=5, size=n_words)
            self.__y_array = np.random.uniform(
                low=-5, high=5, size=n_words)
        elif self.__shape == "c":
            self.__x_array = r_squared * np.cos(theta)
            self.__y_array = r_squared * np.sin(theta)

        return self.__x_array, self.__y_array
