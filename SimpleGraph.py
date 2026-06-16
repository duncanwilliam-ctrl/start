# plotting a graph in Python
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]


plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Graph')


plt.show()
