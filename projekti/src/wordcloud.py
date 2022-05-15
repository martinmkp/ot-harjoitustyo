import matplotlib.pyplot as plt
from adjustText import adjust_text


class WordCloud:
    """
    Contains the functionalities to plot a wordcloud.

    Attributes:
        word_count: A list of word counts for each word.
        x_array: X-coordinates for the word cloud.
        y_array: Y-coordinates for the word cloud.
    """

    def __init__(self, word_count, x_array, y_array):
        """Constructor for creating a word cloud.

        Args:
            word_count: A list of word counts for each word.
            x_array: X-coordinates for the word cloud.
            y-array: Y-coordinates for the word cloud.
        """
        self.__word_counts = word_count
        self.__fig = None
        self.__cloud_texts = []
        self.__adjust_text = adjust_text
        self.axes = None
        self.x_array = x_array
        self.y_array = y_array

    def plot_words(self, filename):
        """Plots and saves a wordcloud as a .png file.
        """
        colors = ["#EF4026", "#0343DF", "#DAA520", "darkgreen"]
        curr_color = ""

        self.__fig, self.axes = plt.subplots(figsize=(8, 8))
        self.axes.scatter(self.x_array, self.y_array,
                          color='white', marker=',')
        self.axes.axis('off')

        for i, label in enumerate(list(self.__word_counts)):
            if i < len(self.__word_counts) // 4:
                curr_color = colors[0]
            elif i < len(self.__word_counts) // 2:
                curr_color = colors[1]
            elif i < 3 * len(self.__word_counts) // 4:
                curr_color = colors[2]
            else:
                curr_color = colors[3]
            self.__cloud_texts.append(self.axes.annotate(label[0],
            (self.x_array[i], self.y_array[i]),size=8+label[1]*3, color=curr_color))

        self.__adjust_text(self.__cloud_texts)
        self.__fig.savefig(f"word_clouds/{filename}.png")
