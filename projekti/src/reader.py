import os
import numpy as np
import matplotlib.pyplot as plt


class Reader:
    """
    This class teads a .txt file to a string variable.
    """

    def __init__(self):
        self.text = ""

    def read_txt(self, dir, encode="utf-8"):
        """
        Reads a txt-file
        """
        fullpath = os.path.join(os.getcwd()[:-9], dir)
        print("Reading the data file from the path:\n", fullpath)
        try:
            with open(fullpath, encoding=encode) as file:
                self.text = ''.join(file.readlines())
            print("\nText data read successfully.")
            return self.text

        except Exception as e:
            print("An exception occurred:\n", e)
