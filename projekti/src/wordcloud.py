import numpy as np
import os

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


    def read_txt(self, directory, filename, encode = "utf-8"):
        """
        Reads a txt-file
        """
        print("Reading the text data...")
        fullpath = os.path.join(directory, filename)
        try:
            with open(fullpath, encoding = encode) as file:
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
        self.word_counts = { word : 0 for word in set(self.text_list) }
        for word in self.text_list:
            self.word_counts[word] += 1
        self.word_counts = sorted(self.word_counts.items(), key = lambda x: x[1], reverse=True)


    def set_coordinates(self):
        """
        Sets random coordinates for the words.
        """
        x_array = np.random.uniform(low = -5, high = 5, size = len(self.word_counts))
        y_array = np.random.uniform(low = -5, high = 5, size = len(self.word_counts))

        for i in range(len(self.word_counts)):
            self.coordinate_dict[self.word_counts[i][0]] = (x_array[i], y_array[i])



if __name__ == "__main__":
    # absolute directory
    dir = "/home/martin/Desktop/Ohjelmistotekniikka 2022/ot-harjoitustyo/projekti/data_folder"
    # filename
    file = "tekstidata.txt"
    wordcloud = WordCloud()
    wordcloud.read_txt(dir, file)
    wordcloud.modify_text()
    wordcloud.count_words()
    wordcloud.set_coordinates()
