import os


class Reader:
    """
    This class teads a .txt file to a string variable.
    """

    def __init__(self):
        self.text = ""

    def read_txt(self, directory, encode="utf-8"):
        """
        Reads a txt-file
        """
        fullpath = os.path.join(os.getcwd()[:-9], directory)
        try:
            with open(fullpath, encoding=encode) as file:
                self.text = ''.join(file.readlines())
            return self.text

        except FileNotFoundError:
            print("An exception occurred:\n", FileNotFoundError)
            return None
