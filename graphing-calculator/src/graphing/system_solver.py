from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np

def solve_system(equations):
    # Solve a system of equations
    symbols_list = symbols('x y')
    solutions = solve(equations, symbols_list)
    return solutions

def plot_system(equations, x_range=(-10, 10), y_range=(-10, 10)):
    # Plot the system of equations
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    for eq in equations:
        y_vals = [float(solve(eq.subs('x', x), 'y')) for x in x_vals]
        plt.plot(x_vals, y_vals, label=str(eq))

    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title('Graph of the System of Equations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()