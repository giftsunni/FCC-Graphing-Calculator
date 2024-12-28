from sympy import symbols, Eq, solve

def solve_linear_equation(a, b, c):
    # Solve the linear equation ax + b = c
    x = symbols('x')
    equation = Eq(a * x + b, c)
    return solve(equation, x)[0]

def solve_system_of_equations(eq1, eq2):
    # Solve a system of linear equations
    return solve((eq1, eq2))