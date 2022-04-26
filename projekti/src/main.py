import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from data_setup import SetUp
from reader import Reader
from database import DataBase


def main():
    dir = "projekti/data_folder/tekstidata.txt"

    print("Read data from a text file (t) or an sqlite database (s)?")
    data_reading = input("(t/s): ")

    if data_reading == "t":
        # Reads data from a text file
        reader = Reader()
        text_data = reader.read_txt(dir)

        # Prepares data for wordcloud
        setup = SetUp(text_data)
        setup.modify_text()
        setup.string_to_list()
        words_count = setup.count_words()
        x_coordinates, y_coordinates = setup.set_coordinates()

    elif data_reading == "s":
        db = DataBase()
        db.connect_db()
        print("The datasets in the sqlite database are:")
        db.read_dataset_names_from_db()
        column_name = input("Please give the name of the dataset: ")
        x_coordinates, y_coordinates, words_count = db.read_from_db(
            column_name)

    # Creates a word cloud, and saves it as a .png file
    print("\nCreating a wordcloud...")
    wordcloud = WordCloud(words_count, x_coordinates, y_coordinates)
    wordcloud.plot_words()
    print("Wordcloud created and saved successfully.")

    # Saves the coordinates and the word count of the word cloud
    # To an sqlite database
    teksti = input(
        "Save coordinates and word count to a sqlite database? (y/n): ")
    if teksti == "y":
        db = DataBase()
        db.connect_db()
        nimi = input("Please give a name for the sqlite insertion: ")
        db.save_to_db(nimi, str(x_coordinates),
                      str(y_coordinates), str(words_count))
        print("Coordinates and word counts saved to the database.")


if __name__ == "__main__":
    main()
