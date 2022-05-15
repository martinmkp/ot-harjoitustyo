import glob
import os
from wordcloud import WordCloud
from data_setup import SetUp
from reader import Reader
from database import DataBase


class TextInterface():
    """Contains a method to execute the application through command line,
    i.e., the text user interface.

    Attributes:
        directory: directory for the text data file
    """

    def __init__(self, data_path):
        """Constructor for text interface.

        Args:
            directory: directory for the text data file
        """
        self.data_path = data_path
        self.x_coordinates = None
        self.y_coordinates = None
        self.words_count = None
        self.data_source_type = ""
        self.wordcloud_filename = ""
        self.db_question = ""
        self.textdata_name = ""
        self.row_name = ""
        self.text_data = None
        self.shape = ""

    def execute_data_preprocessing(self):
        """Executes data preprocessing for wordcloud creation.
        """
        while self.data_source_type not in ["s", "t"]:
            print("Read data from a text file (t) or an sqlite database (s)?")
            self.data_source_type = input("(t/s): ")

            if self.data_source_type not in ["s", "t"]:
                print("Input must be  't' or 's'.")

        if self.data_source_type == "t":
            reader = Reader()
            print("List of available .txt files:")
            txt_files = [os.path.basename(x) for x in glob.glob(
                f"{os.getcwd()}/data_folder/*.txt")]
            print(txt_files)

            while self.textdata_name not in txt_files:
                self.textdata_name = input(
                    "Please give the name of the text dataset (including a filename extension): ")
                if self.textdata_name not in txt_files:
                    print("Filename not found. Please try again.")

            while self.shape not in ["s", "c"]:
                self.shape = input(
                    "Please give a shape for the word cloud (s for square, c for circle ): ")
                if self.shape not in ["s", "c"]:
                    print("The input must be either 'c' or 's'.")

            self.text_data = reader.read_txt(
                self.data_path + self.textdata_name)
            setup = SetUp(self.text_data, self.shape)
            setup.modify_text()
            setup.string_to_list()
            self.words_count = setup.count_words()
            self.x_coordinates, self.y_coordinates = setup.set_coordinates()

        elif self.data_source_type == "s":
            database = DataBase()
            database.connect_db()
            print("The datasets in the sqlite database are:")
            database.read_dataset_names_from_db()
            while self.row_name not in database.wordcloud_names:
                self.row_name = input("Please give the name of the dataset: ")
                if self.row_name not in database.wordcloud_names:
                    print("Dataset doesn't exist. Please try a different input.")
            self.x_coordinates, self.y_coordinates, self.words_count = database.read_from_db(
                self.row_name)

        return self.x_coordinates, self.y_coordinates, self.words_count

    def execute_wordcloud_creation(self):
        """Executes the wordcloud creation and saving.
        """
        wordcloud = WordCloud(
            self.words_count, self.x_coordinates, self.y_coordinates)

        while len(self.wordcloud_filename) < 1:
            self.wordcloud_filename = input(
                "Please give a name for the wordcloud (without a filename extension): ")

        print("\nCreating a wordcloud...")
        wordcloud.plot_words(self.wordcloud_filename)
        print("Wordcloud created and saved successfully.")

        while self.db_question not in ["y", "n"]:
            self.db_question = input(
                "Save coordinates and word count to a sqlite database? (y/n): ")
            if self.db_question not in ["y", "n"]:
                print("Input must be 'y' or 'n'")

        if self.db_question == "y":
            database = DataBase()
            database.connect_db()
            nimi = input("Please give a name for the sqlite insertion: ")
            database.save_to_db(nimi, str(self.x_coordinates),
                                str(self.y_coordinates), str(self.words_count))
            print("Coordinates and word counts saved to the database.")
