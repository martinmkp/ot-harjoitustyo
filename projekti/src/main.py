from ui_text import TextInterface

DATA_PATH = "projekti/data_folder/"


def main(data_path):
    text_interface = TextInterface(data_path)
    text_interface.execute_data_preprocessing()
    text_interface.execute_wordcloud_creation()
    return True


if __name__ == "__main__":
    main(DATA_PATH)
