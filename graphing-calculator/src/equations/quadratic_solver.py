from sympy import symbols, Eq, solve

def solve_quadratic(a, b, c):
    # Solve the quadratic equation ax^2 + bx + c = 0
    x = symbols('x')
    equation = Eq(a*x**2 + b*x + c, 0)
    solutions = solve(equation, x)
    return solutions

def vertex_form(a, b, c):
    # Convert to vertex form y = a(x - h)^2 + k
    h = -b / (2 * a)
    k = (4 * a * c - b**2) / (4 * a)
    return (h, k)

def discriminant(a, b, c):
    # Calculate the discriminant of the quadratic equation
    return b**2 - 4*a*c

def is_real_solution(a, b, c):
    # Check if the quadratic equation has real solutions
    return discriminant(a, b, c) >= 0