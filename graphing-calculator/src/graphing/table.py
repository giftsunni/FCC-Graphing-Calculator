from sympy import symbols

def generate_table(func, x_values):
    x = symbols('x')
    table = []
    for x_val in x_values:
        y_val = func(x_val)
        table.append((x_val, y_val))
    return table

def print_table(table):
    print(" x |   y")
    print("---------")
    for x_val, y_val in table:
        print(f"{x_val:>2} | {y_val}")