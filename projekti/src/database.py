import os
import sqlite3
import json


class DataBase:
    def __init__(self, path=os.getcwd()[:-9], db_path="projekti/database_sql/wordcloud_db.db"):
        self.fullpath = os.path.join(path, db_path)
        self.connection = None
        self.cursor = None

    def connect_db(self):
        """
        Connects the database.
        """
        self.connection = sqlite3.connect(self.fullpath)
        self.cursor = self.connection.cursor()

    def create_db(self):
        """
        Creates a table for wordclouds.
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
        insert_table = f"""
        INSERT INTO Wordclouds (name, x_coord, y_coord, word_counts)
        VALUES (?, ?, ?, ?)
        """
        try:
            self.cursor.execute(insert_table,
                                (name, x_coord, y_coord, word_counts))
        except Exception as e:
            print("An exception occurred:\n", e)

    def coordinates_manipulation(self, old_string):
        new_string = old_string.replace("[", "")
        new_string = new_string.replace("]", "")
        new_string = new_string.replace("\n", "")
        new_list = list(new_string.split(' '))
        new_list = [x for x in new_list if len(x) > 3]
        new_list = [float(x) for x in new_list]
        return new_list

    def word_count_manipulation(self, old_string):
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
        dataset_names = "SELECT name FROM Wordclouds;"
        try:
            self.cursor.execute(dataset_names)
            names = self.cursor.fetchall()
            self.connection.commit()
            print(names)

        except Exception as e:
            print("An exception occurred:\n", e)

    def read_from_db(self, name):
        read_table = "SELECT * FROM Wordclouds WHERE name=?;"
        try:
            self.cursor.execute(read_table, [name])
            output = self.cursor.fetchall()
            self.connection.commit()

            x_coordinates = self.coordinates_manipulation(output[0][2])
            y_coordinates = self.coordinates_manipulation(output[0][3])
            word_count = self.word_count_manipulation(output[0][4])

            return (x_coordinates, y_coordinates, word_count)

        except Exception as e:
            print("An exception occurred:\n", e)


if __name__ == "__main__":
    database = DataBase()
    database.connect_db()
