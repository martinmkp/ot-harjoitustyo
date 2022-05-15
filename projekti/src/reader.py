import os


class Reader:
    """
    Reads a .txt file to a string variable from the given path.
    """

    def __init__(self):
        self.__text = ""

    def read_txt(self, directory, encode="utf-8"):
        """Returns a string variable containing data from the given path.
        It is assumed that the file is a text-file.

        Args:
            directory: Directory of a textfile.
            encode: Encoding of the textfile. Set to utf-8 by default.
        """
        fullpath = os.path.join(os.getcwd()[:-9], directory)
        try:
            with open(fullpath, encoding=encode) as file:
                self.__text = ''.join(file.readlines())
            return self.__text

        except FileNotFoundError:
            print("An exception occurred:\n", FileNotFoundError)
            return None
