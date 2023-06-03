# Linear Equation Solver

## Overall, this code provides a basic implementation of Gaussian elimination and reduced row echelon form to solve systems of linear equations. It can be extended and customized to suit specific needs and further enhanced with additional functionality as required.

### It contains several methods  for solving linear equations namely:
1- getting_input

2- smallest_pivot_position

3- greatest_pivot_position

4- swap_rows

5- rows_operations

6- row_reduce_1

7- pivot_finder

8- equation_solver

9- find_coefficient

10- is_consistent

11- forward_phase

12- backward_phase

13- reduced_echelon_form

14- solve

### Detail of each function
1-The getting_input method prompts the user to enter the number of equations and the coefficients of each equation. It reads the input values and constructs a matrix using 

2- The smallest_pivot_position method finds the position of the smallest pivot in the matrix, given a specific row number. It iterates over the rows below the specified row, identifies the first non-zero element in each row, and returns the position of the smallest non-zero element.

3- The greatest_pivot_position method works similarly to smallest_pivot_position, but it finds the position of the greatest pivot instead.

4- The swap_rows method swaps the positions of two rows in the matrix. It temporarily stores one row in a temporary variable, replaces it with the other row, and then replaces the other row with the stored row.

5-The rows_operations method performs row operations on two rows. It takes the sum of one row and the product of the other row with a given operand and assigns the result to the second row.

6- The row_reduce_1 method divides a row by a specified operand, resulting in the row being scaled down.

7- The pivot_finder method finds the positions of all the non-zero pivots (first non-zero elements) in the matrix. It iterates over each row, identifies the first non-zero element, and stores its position.

8-The equation_solver method solves the system of linear equations using the matrix in reduced row echelon form. It takes the positions of the pivots as input and calculates the values of the variables based on the given system of equations.

9- The find_coefficient method calculates the coefficient used in row operations to eliminate a variable during the forward and backward phase of the algorithm.

10- The is_consistent method checks if the system of equations is consistent or not. It checks the last row of the matrix to see if there is a non-zero element in the last column (the augmented column). If there is no non-zero element, it means the system is inconsistent.

11- The forward_phase method performs the forward phase of the Gaussian elimination algorithm. It iterates over each row, finds the smallest pivot, swaps rows if necessary, and performs row operations to eliminate variables below the pivot.

12- The backward_phase method performs the backward phase of the Gaussian elimination algorithm. It iterates over each row in reverse order, finds the greatest pivot, and performs row operations to eliminate variables above the pivot.

13- The reduced_echelon_form method transforms the matrix into reduced row echelon form by performing additional row reduction operations. It first ensures that the pivots are in the correct positions and then scales each pivot to 1.

14- The solve method serves as the main entry point for solving the system of linear equations. It calls the necessary methods in the correct order to perform Gaussian elimination, reduce the matrix to row echelon form, and solve the equations.
