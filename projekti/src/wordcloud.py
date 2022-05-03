import matplotlib.pyplot as plt


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
        self.word_counts = word_count
        self.x_array = x_array
        self.y_array = y_array
        self.fig = None
        self.axes = None

    def plot_words(self, filename):
        """
        Plots and saves a wordcloud as a .png file. 
        """
        colors = ["#069AF3", "#13EAC9", "#90EE90", "#00FF00"]
        curr_color = ""

        self.fig, self.axes = plt.subplots()
        self.axes.scatter(self.x_array, self.y_array,
                          color='white', marker=',')

        for i, label in enumerate(list(self.word_counts)):
            if i < len(self.word_counts) // 4:
                curr_color = colors[0]
            elif i < len(self.word_counts) // 2:
                curr_color = colors[1]
            elif i < 3 * len(self.word_counts) // 4:
                curr_color = colors[2]
            else:
                curr_color = colors[3]
            self.axes.annotate(label[0], (self.x_array[i], self.y_array[i]),
                               size=8+label[1]*3, color=curr_color)
        print(self.axes)
        self.fig.savefig(f"word_clouds/{filename}.png")
