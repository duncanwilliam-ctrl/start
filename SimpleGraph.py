# plotting a graph in Python
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [20, 30, 45, 50, 52]
x2 = [6, 8, 10, 12, 14]
y2 = [10, 20, 30, 35, 70]


# plot creates a line graph, scatter is a scatter chart, bar is a bar chart, hist is a histogram, pie is a pie chart
# you can customize the graph by changing the color, line width, marker style, and more. You can also add labels and a title to the graph.
# the axhline function adds a horizontal line to the graph at a specified y-value, in this case, 40. The color and linestyle of the line can also be customized.
# the savefig function saves the current figure to a file. The filename and format can be specified, as well as the resolution (dpi) of the saved image.


plt.plot(x, y, c="orange", linewidth=3, marker='o',
         markersize=8, label='Line 1', linestyle='--')
plt.plot(x2, y2, c="blue", linewidth=0.5,
         marker='s', markersize=8, label='Line 2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Graph')
plt.axhline(40, color='green', linestyle='--')


# this will save the plot as a PNG file
plt.savefig('simple_graph.png', dpi=300)


plt.show()  # this will show the plot in a window
