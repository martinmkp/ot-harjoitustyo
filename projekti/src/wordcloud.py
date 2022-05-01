import matplotlib.pyplot as plt


class WordCloud:
    """
    Contains the functionalities to plot a wordcloud.

    Attributes:
        word_count: A list of word counts for each word.
        x_array: X-coordinates for the word cloud.
        y-array: Y-coordinates for the word cloud.
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

    def plot_words(self):
        """
        Plots and saves a wordcloud as a .png file. 
        """
        # Set up colors
        colors = ["#069AF3", "#13EAC9", "#90EE90", "#00FF00"]
        curr_color = ""

        # Set up the plot
        fig, axes = plt.subplots()
        axes.scatter(self.x_array, self.y_array, color='white', marker=',')

        # Add the words to the invisible markers in the plot as annotations
        for i, label in enumerate(list(self.word_counts)):
            if i < len(self.word_counts) // 4:
                curr_color = colors[0]
            elif i < len(self.word_counts) // 2:
                curr_color = colors[1]
            elif i < 3 * len(self.word_counts) // 4:
                curr_color = colors[2]
            else:
                curr_color = colors[3]
            axes.annotate(label[0], (self.x_array[i], self.y_array[i]),
                          size=8+label[1]*3, color=curr_color)

        # Removes the axis
        axes.axis("off")
        # Saves the figure
        fig.savefig("sanapilvi.png")
