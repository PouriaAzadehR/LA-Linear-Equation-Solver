# Linear Equation Solver

### Overall, this code provides a basic implementation of Gaussian elimination and reduced row echelon form to solve systems of linear equations. It can be extended and customized to suit specific needs and further enhanced with additional functionality as required.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## INPUT & OUTPUT 

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/5c7d6f28-acda-461d-bd09-b0c2971d9e8d)


![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/75141c2e-9dbf-4b68-86d7-1996b123ea82)


It should be noiced that free variables are equal to 10

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/3ed46df0-7f26-4c2b-a26c-e7db2f88dbd0)














----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/36156b9c-cf3a-4693-a000-ed65817894b2)




2- The smallest_pivot_position method finds the position of the smallest pivot in the matrix, given a specific row number. It iterates over the rows below the specified row,identifies the first non-zero element in each row, and returns the position of the smallest non-zero element.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/6fdc243f-028a-4abf-9495-accaadc5df6e)



3- The greatest_pivot_position method works similarly to smallest_pivot_position, but it finds the position of the greatest pivot instead.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/80fc3648-bc95-48a4-af2c-95a69a74e2eb)



4- The swap_rows method swaps the positions of two rows in the matrix. It temporarily stores one row in a temporary variable, replaces it with the other row, and then replaces the other row with the stored row.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/4a3a470f-e160-4b60-841d-716c8c2aa222)



5-The rows_operations method performs row operations on two rows. It takes the sum of one row and the product of the other row with a given operand and assigns the result to the second row.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/d4ba272b-d865-43f2-a977-0da4ce4ca315)


6- The row_reduce_1 method divides a row by a specified operand, resulting in the row being scaled down.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/a4c15de7-5523-4ee3-9bc0-833b1a99ce30)



7- The pivot_finder method finds the positions of all the non-zero pivots (first non-zero elements) in the matrix. It iterates over each row, identifies the first non-zero element, and stores its position.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/e487cd4e-b955-4c2e-9919-63d6922dfc35)


8-The equation_solver method solves the system of linear equations using the matrix in reduced row echelon form. It takes the positions of the pivots as input and calculates the values of the variables based on the given system of equations.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/c78ad840-1312-4885-bd70-99062a31561e)



9- The find_coefficient method calculates the coefficient used in row operations to eliminate a variable during the forward and backward phase of the algorithm.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/09509830-532a-4aa7-857f-f363f49f4e03)



10- The is_consistent method checks if the system of equations is consistent or not. It checks the last row of the matrix to see if there is a non-zero element in the last column (the augmented column). If there is no non-zero element, it means the system is inconsistent.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/98d01ff0-4558-4486-a34b-bc1402d0ee31)



11- The forward_phase method performs the forward phase of the Gaussian elimination algorithm. It iterates over each row, finds the smallest pivot, swaps rows if necessary, and performs row operations to eliminate variables below the pivot.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/f966c240-e167-4e99-b75c-6304ce58f2ed)



12- The backward_phase method performs the backward phase of the Gaussian elimination algorithm. It iterates over each row in reverse order, finds the greatest pivot, and performs row operations to eliminate variables above the pivot.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/dddf8791-73da-44b3-8e84-814a41ce13f0)



13- The reduced_echelon_form method transforms the matrix into reduced row echelon form by performing additional row reduction operations. It first ensures that the pivots are in the correct positions and then scales each pivot to 1.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/1159fd94-dd93-4333-8909-ee9aac4dd3a7)




14- The solve method serves as the main entry point for solving the system of linear equations. It calls the necessary methods in the correct order to perform Gaussian elimination, reduce the matrix to row echelon form, and solve the equations.

![image](https://github.com/PouriaAzadehR/LA-Linear-Equation-Solver/assets/93463377/a0f953bb-16b3-4e39-b6e8-770d20c8b929)
