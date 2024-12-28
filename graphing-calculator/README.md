# Graphing Calculator

## Overview
This project is a graphing calculator that allows users to graph one or more mathematical functions, create tables of (x, y) values, shade areas above or below the lines, solve and graph systems of equations, zoom in or out on graphs, and solve quadratic equations.

## Features
- Graph one or more functions
- Generate a table of (x, y) values
- Shade areas above or below the plotted lines
- Solve and graph systems of equations
- Zoom in and out on graphs
- Solve quadratic equations

## Project Structure
```
graphing-calculator
├── src
│   ├── main.py
│   ├── graphing
│   │   ├── __init__.py
│   │   ├── plot.py
│   │   ├── table.py
│   │   ├── shading.py
│   │   ├── system_solver.py
│   │   └── zoom.py
│   ├── equations
│   │   ├── __init__.py
│   │   ├── quadratic_solver.py
│   │   └── linear_solver.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd graphing-calculator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the graphing calculator, execute the following command:
```
python src/main.py
```

## Dependencies
- Matplotlib
- NumPy

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.