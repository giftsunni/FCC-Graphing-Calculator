from matplotlib import pyplot as plt
import numpy as np

def plot_function(func, x_range, label=None):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)
    plt.plot(x, y, label=label)

def plot_multiple_functions(functions, x_range):
    for func, label in functions:
        plot_function(func, x_range, label)
    plt.legend()
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of Functions')
    plt.show()