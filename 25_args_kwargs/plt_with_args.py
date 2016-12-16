#! usr/bin/env python3

import matplotlib.pyplot as plt

def graph_operation(x, y):
    print("Function that graphs {} and {}".format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [4, 5, 6]

x_and_y = [x1, y1]


# Implicit use of *args
graph_operation(*x_and_y)
