from wordcloud import WordCloud
from data_setup import SetUp
from reader import Reader
from database import DataBase


def main():
    directory = "projekti/data_folder/tekstidata.txt"

    while True:
        print("Read data from a text file (t) or an sqlite database (s)?")
        data_reading = input("(t/s): ")

        if data_reading == "t":
            # Reads data from a text file
            reader = Reader()
            text_data = reader.read_txt(directory)

            # Prepares data for wordcloud
            setup = SetUp(text_data)
            setup.modify_text()
            setup.string_to_list()
            words_count = setup.count_words()
            x_coordinates, y_coordinates = setup.set_coordinates()
            break

        elif data_reading == "s":
            database = DataBase()
            database.connect_db()
            print("The datasets in the sqlite database are:")
            database.read_dataset_names_from_db()
            column_name = input("Please give the name of the dataset: ")
            x_coordinates, y_coordinates, words_count = database.read_from_db(
                column_name)
            break
        else:
            print("Input must be  't' or 's'.")

    # Creates a word cloud, and saves it as a .png file
    print("\nCreating a wordcloud...")
    wordcloud = WordCloud(words_count, x_coordinates, y_coordinates)
    wordcloud.plot_words()
    print("Wordcloud created and saved successfully.")

    # Saves the coordinates and the word count of the word cloud
    # To an sqlite database
    while True:
        teksti = input(
            "Save coordinates and word count to a sqlite database? (y/n): ")
        if teksti == "y":
            database = DataBase()
            database.connect_db()
            nimi = input("Please give a name for the sqlite insertion: ")
            database.save_to_db(nimi, str(x_coordinates),
                                str(y_coordinates), str(words_count))
            print("Coordinates and word counts saved to the database.")
            break
        elif teksti == "n":
            break
        else:
            print("Input must be 'y' or 'n'")


if __name__ == "__main__":
    main()
