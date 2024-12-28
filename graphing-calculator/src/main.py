from graphing.plot import plot_functions
from graphing.table import generate_table
from graphing.shading import shade_area
from graphing.system_solver import solve_system
from graphing.zoom import zoom_graph
from equations.quadratic_solver import solve_quadratic
from equations.linear_solver import solve_linear
from utils.helpers import get_user_input

def main():
    print("Welcome to the Graphing Calculator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Graph functions")
        print("2. Generate table of (x, y) values")
        print("3. Shade area above/below a function")
        print("4. Solve and graph a system of equations")
        print("5. Zoom in/out on a graph")
        print("6. Solve quadratic equations")
        print("7. Solve linear equations")
        print("8. Exit")
        
        choice = get_user_input("Enter your choice (1-8): ")
        
        if choice == '1':
            functions = get_user_input("Enter functions to graph (comma-separated): ").split(',')
            plot_functions(functions)
        elif choice == '2':
            function = get_user_input("Enter function to generate table for: ")
            x_values = list(map(float, get_user_input("Enter x values (comma-separated): ").split(',')))
            table = generate_table(function, x_values)
            print(table)
        elif choice == '3':
            function = get_user_input("Enter function to shade: ")
            area = get_user_input("Shade above or below? (above/below): ")
            shade_area(function, area)
        elif choice == '4':
            equations = get_user_input("Enter equations (comma-separated): ").split(',')
            solutions = solve_system(equations)
            plot_functions(equations)
            print("Solutions:", solutions)
        elif choice == '5':
            zoom_level = float(get_user_input("Enter zoom level (positive to zoom in, negative to zoom out): "))
            zoom_graph(zoom_level)
        elif choice == '6':
            equation = get_user_input("Enter quadratic equation (e.g., ax^2 + bx + c = 0): ")
            solutions = solve_quadratic(equation)
            print("Solutions:", solutions)
        elif choice == '7':
            equation = get_user_input("Enter linear equation (e.g., ax + b = c): ")
            solution = solve_linear(equation)
            print("Solution:", solution)
        elif choice == '8':
            print("Exiting the Graphing Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()