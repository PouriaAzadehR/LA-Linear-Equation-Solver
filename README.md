# Linear Equation Solver

This Python program solves a system of linear equations using the Gaussian elimination method. It provides various functions to perform different operations on the matrix representing the system of equations.

## Installation

To run the Linear Equation Solver program, make sure you have Python installed on your system. No additional libraries or dependencies are required.

1. Clone the repository:

   ```shell
   git clone https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver.git
   ```

2. Navigate to the project directory:

   ```shell
   cd LA-Linear-Equation-Solver
   ```

## Usage

1. Open the `main.py` file in a text editor.

2. Modify the `getting_input` function to provide the input for the system of linear equations. Enter the number of equations (`num_of_equations`) and the coefficients of each equation in the `matrix_of_equation` list.

3. Save the file.

4. Run the program:

   ```shell
   python main.py
   ```

5. The program will display the solution for the variables in the system of linear equations.

## Functions

The Linear Equation Solver program consists of the following functions:

### `getting_input`

This function takes input from the user for the system of linear equations. It prompts the user to enter the number of equations and the coefficients of each equation. The input is stored in the `matrix` variable as a NumPy matrix.

### `smallest_pivot_position`

This function finds the smallest pivot position (row and column) for the Gaussian elimination. It iterates through the rows of the matrix starting from a given row and returns the position of the smallest pivot.

### `greatest_pivot_position`

This function finds the greatest pivot position (row and column) for the backward phase of Gaussian elimination. It iterates through the rows of the matrix starting from a given row and returns the position of the greatest pivot.

### `swap_rows`

This function swaps two rows in the matrix. It takes the original row and the row to be swapped as input and performs the swap operation using a temporary variable.

### `rows_operations`

This function performs row operations on the matrix. It takes two rows and an operand as input and performs the operation `row2 = row2 + row1 * operand`.

### `row_reduce_1`

This function reduces a row by dividing all its elements by a given operand. It performs the operation `row = row / operand` to normalize the row.

### `pivot_finder`

This function finds all the pivot positions in the matrix. It iterates through the rows and checks for the first non-zero element in each row. It returns a list of all pivot positions.

### `equation_solver`

This function solves the system of linear equations using the pivot positions. It calculates the solution for each variable by subtracting the product of the coefficients and the corresponding values from the constant term. It also handles the variables that are not included in the pivot positions.

### `find_coefficient`

This function calculates the coefficient used for row operations during the Gaussian elimination. It checks if the pivot element is zero and returns `None` if it is. Otherwise, it calculates and returns the coefficient.

### `is_consistent`

This function checks if the matrix is consistent, i.e., if the system of linear equations has a solution. It checks if the last row of the matrix has a non-zero element in the last column.

### `forward_phase`

This function performs the forward phase of Gaussian elimination. It iterates through the rows of the matrix, finds the smallest pivot position, and performs row operations to eliminate the coefficients below the pivot.

### `backward_phase`

This function performs the backward phase of Gaussian elimination. It iterates through the rows of the matrix in

 reverse order, finds the greatest pivot position, and performs row operations to eliminate the coefficients above the pivot.

### `reduced_echelon_form`

This function converts the matrix to reduced row echelon form. It swaps rows to bring the smallest pivot elements to the upper-left corner and performs row reduction to make all other elements in the same column zero.

### `solve`

This function solves the system of linear equations. It calls the necessary functions in the required order to perform Gaussian elimination and obtain the solution for the variables. It also displays whether the matrix is consistent or not.

## Example

Let's consider the following system of linear equations:

```
2x + 3y - z = 1
x - y + 2z = 3
3x + 2y - 4z = 4
```

To solve this system, modify the `getting_input` function as follows:

```python
def getting_input(self):
    self.num_of_equations = 3
    matrix_of_equation = [
        [2, 3, -1, 1],
        [1, -1, 2, 3],
        [3, 2, -4, 4]
    ]
    self.matrix = np.matrix(matrix_of_equation, dtype=np.float64)
```

Save the file and run the program. The solution will be displayed as:

```
x[1]: 1.0
x[2]: 2.0
x[3]: -1.0
```

This indicates that `x = 1.0`, `y = 2.0`, and `z = -1.0` are the solutions to the system of linear equations.


## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## Contact

For any questions or inquiries, please contact [pouriazadeh81@gmail.com](mailto:pouriazadeh81@gmail.com).
