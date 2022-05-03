import os
import sqlite3


class DataBase:
    """A class for an sqlite database. This database
    is used to store information about created word clouds.

    Attributes:
        path: Absolute aath to this project
        db_path: Relative path to a .db file.
    """

    def __init__(self, path=os.getcwd()[:-9], db_path="projekti/database_sql/wordcloud_db.db"):
        """Constructor for creating a database.

        Args:
            path: Absolute aath to this project
            db_path: Relative path to a .db file.
        """
        self.fullpath = os.path.join(path, db_path)
        self.connection = None
        self.cursor = None
        self.wordcloud_names = []

    def connect_db(self):
        """Connects the database.
        """
        self.connection = sqlite3.connect(self.fullpath)
        self.cursor = self.connection.cursor()

    def create_db(self):
        """Creates a table for wordclouds.
        """
        create_table = """
        CREATE TABLE IF NOT EXISTS Wordclouds 
        (id INTEGER PRIMARY KEY,
        name TEXT,
        x_coord TEXT,
        y_coord TEXT,
        word_counts TEXT);"""
        self.cursor.execute(create_table)
        self.connection.commit()

    def save_to_db(self, name, x_coord, y_coord, word_counts):
        """Saves word cloud information to the database.

        Args:
            name: Name for a word cloud.
            x_coord: X-coordinates of a word cloud.
            y_coorx: Y-coordinates of a word cloud.
            word_counts: Frequency of each word in the dataset.
        """
        insert_table = """
        INSERT INTO Wordclouds (name, x_coord, y_coord, word_counts)
        VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(insert_table,
                            (name, x_coord, y_coord, word_counts))

    def coordinates_manipulation(self, old_string):
        """Manipulates the queried coordinates to a list form.

        Args:
            old_string: The initially queried coordinates.
        """
        new_string = old_string.replace("[", "")
        new_string = new_string.replace("]", "")
        new_string = new_string.replace("\n", "")
        new_list = list(new_string.split(' '))
        new_list = [x for x in new_list if len(x) > 3]
        new_list = [float(x) for x in new_list]
        return new_list

    def word_count_manipulation(self, old_string):
        """Manipulates the queried word count to a list form.

        Args:
            old_string: The initially queried coordinates.
        """
        new_string = old_string.replace("[", "")
        new_string = new_string.replace("]", "")
        new_string = new_string.replace("\n", "")
        new_string = new_string.replace(",", "")
        new_string = new_string.replace("(", "")
        new_string = new_string.replace(")", "")
        new_string = new_string.replace("'", "")
        new_list = list(new_string.split(' '))
        result_list = []
        for i in range(0, len(new_list)-2, 2):
            element = tuple((new_list[i], int(new_list[i+1])))
            result_list.append(element)

        return result_list

    def read_dataset_names_from_db(self):
        """Executes a SELECT query from a db to get a list of names.
        """
        dataset_names = "SELECT name FROM Wordclouds;"
        self.cursor.execute(dataset_names)
        names = self.cursor.fetchall()
        self.connection.commit()
        for name in names:
            self.wordcloud_names.append(name[0])
        print(self.wordcloud_names)

    def read_from_db(self, name):
        """Executes a SELECT query from adb to get information
        of a specific word cloud.

        Args:
            name: Name of a word cloud.
        """
        read_table = "SELECT * FROM Wordclouds WHERE name=?;"
        while True:
            if name in self.wordcloud_names:
                self.cursor.execute(read_table, [name])
                output = self.cursor.fetchall()
                self.connection.commit()

                x_coordinates = self.coordinates_manipulation(output[0][2])
                y_coordinates = self.coordinates_manipulation(output[0][3])
                word_count = self.word_count_manipulation(output[0][4])
            else:
                name = input("Name not found. Please try again: ")
            return (x_coordinates, y_coordinates, word_count)
