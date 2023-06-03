import numpy as np


class LinearEquationSolver:

    def __init__(self):
        self.num_of_equations = 0
        self.matrix = None

    def getting_input(self):
        self.num_of_equations = int(input())
        matrix_of_equation = []
        for _ in range(self.num_of_equations):
            equation = list(map(int, input().split()))
            matrix_of_equation.append(equation)
        self.matrix = np.matrix(matrix_of_equation, dtype=np.float64)

    def smallest_pivot_position(self, num_row):
        position_of_pivots = []
        for p in range(num_row, (self.matrix.shape[0])):
            m = self.matrix[p].tolist()
            index_first_match = next(
                (index for index, item in enumerate(m[0])
                 if item != 0),
                None
            )
            if index_first_match is None:
                index_first_match = 100000000
            if index_first_match < num_row:
                continue
            position_of_pivots.append((p, index_first_match))
        return min(position_of_pivots, key=lambda tup: tup[1])

    def greatest_pivot_position(self, num_row):
        position_of_pivots = []
        for p in range(num_row, -1, -1):
            m = self.matrix[p].tolist()
            index_first_match = next(
                (index for index, item in enumerate(m[0])
                 if item != 0),
                None
            )
            if index_first_match is None:
                index_first_match = 100000000

            position_of_pivots.append((p, index_first_match))
        return max(position_of_pivots, key=lambda tup: tup[1])

    def swap_rows(self, original_row, swapped_row):
        temp = np.array(self.matrix[original_row], dtype=np.float64)
        self.matrix[original_row] = self.matrix[swapped_row]
        self.matrix[swapped_row] = temp

    def rows_operations(self, row1, row2, operand):
        self.matrix[row2] = self.matrix[row2] + self.matrix[row1] * operand

    def row_reduce_1(self, row, operand):
        self.matrix[row] = self.matrix[row] / operand

    def pivot_finder(self):
        position_of_pivots = []
        for p in range(self.matrix.shape[0]):
            m = self.matrix[p].tolist()
            index_first_match = next(
                (index for index, item in enumerate(m[0])
                 if item != 0),
                None
            )
            if index_first_match is None:
                continue
            position_of_pivots.append((p, index_first_match))
        return position_of_pivots

    def equation_solver(self, position_of_pivots):
        print('dafssssssss \n ', position_of_pivots)
        for pivot in position_of_pivots:
            answer = 0
            for i in range(pivot[1] + 1, self.matrix.shape[1] - 1):
                answer += self.matrix[pivot[0], i] * 10
            final_answer = self.matrix[pivot[0], self.matrix.shape[1] - 1] - answer
            print('x[{}] : {}'.format(pivot[1] + 1, final_answer))
        for j in range(self.matrix.shape[1] - 1):
            flag_in = False
            for pivot in position_of_pivots:
                if j == pivot[1]:
                    flag_in = True
            if not flag_in:
                print('x[{}] : 10'.format(j + 1))

    def find_coefficient(self, i, pivot):
        if self.matrix[pivot[0], pivot[1]] == 0:
            return None
        coefficient_f = -(self.matrix[i, pivot[1]] / self.matrix[pivot[0], pivot[1]])
        print('coefficient_f  ', coefficient_f)
        return coefficient_f

    def is_consistent(self):
        for r in range(self.matrix.shape[0] - 1, -1, -1):
            m = self.matrix[self.matrix.shape[0] - 1].tolist()
            index_first_match = next(
                (index for index, item in enumerate(m[0])
                 if item != 0),
                None
            )
            if index_first_match == self.matrix.shape[1] - 1:
                return False
        return True

    # forward
    def forward_phase(self):
        for r in range(self.matrix.shape[0] - 1):
            pivot = self.smallest_pivot_position(r)
            self.swap_rows(r, pivot[0])
            pivot = self.smallest_pivot_position(r)
            for i in range(pivot[0] + 1, self.matrix.shape[0]):
                if pivot[1] == 100000000:
                    continue
                coefficient = self.find_coefficient(i, pivot)
                if coefficient is not None:
                    self.rows_operations(pivot[0], i, coefficient)

    # backward
    def backward_phase(self):
        for r in range(self.matrix.shape[0] - 1, -1, -1):
            pivot = self.greatest_pivot_position(r)
            if pivot[1] == self.matrix.shape[1] - 1 and pivot[0] == self.matrix.shape[0] - 1:
                continue
            for i in range(pivot[0] - 1, -1, -1):
                if pivot[1] == 100000000:
                    continue
                coefficient = self.find_coefficient(i, pivot)
                if coefficient is not None:
                    self.rows_operations(pivot[0], i, coefficient)

    def reduced_echelon_form(self):
        for r in range(self.matrix.shape[0] - 1):
            pivot = self.smallest_pivot_position(r)
            self.swap_rows(r, pivot[0])
        for r in range(self.matrix.shape[0]):
            pivot = self.smallest_pivot_position(r)
            if pivot[1] == 100000000:
                continue
            if pivot[1] == self.matrix.shape[1] - 1 and pivot[0] == self.matrix.shape[0] - 1:
                continue
            self.row_reduce_1(pivot[0], self.matrix[pivot[0], pivot[1]])

    def solve(self):
        self.getting_input()
        self.forward_phase()
        self.backward_phase()
        self.reduced_echelon_form()
        print('Matrix is consistent: ', self.is_consistent())
        self.equation_solver(self.pivot_finder())


linear_equaion_solver = LinearEquationSolver()
linear_equaion_solver.solve()
