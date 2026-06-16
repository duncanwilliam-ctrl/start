# plotting a graph in Python
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [20, 30, 40, 50, 52]
x2 = [6, 8, 10, 12, 14]
y2 = [10, 20, 30, 40, 70]

plt.plot(x, y, c="orange", linewidth=3, marker='o',
         markersize=8, label='Line 1', linestyle='--')
plt.plot(x2, y2, c="blue", linewidth=0.5,
         marker='s', markersize=8, label='Line 2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Graph')
plt.legend()

plt.show()  # this will show the plot in a window
